"""Server"""
import os
import configparser
from datetime import datetime
from time import sleep
from json import load, dumps
from json.decoder import JSONDecodeError
import datetime

from bottle import route, run, static_file, request, Bottle, abort

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

from application import wows_api_wrapper, ships_info, wows_stats

INIFILE = configparser.SafeConfigParser()
INIFILE.read('./config/config.ini', 'UTF-8')
app_id = INIFILE["config"]["application_id"]
region = INIFILE["config"]["region"]
SI = ships_info.ShipInfo(app_id, region)
WAW = wows_api_wrapper.APIWrapper(app_id, region)

def test(ArenaInfo):
    wst = wows_stats.WoWsStats()
    for vehicle in ArenaInfo["vehicles"]:
        wst.init_user_dict()
        ign = vehicle["name"]
        wst.add_ign(ign)
        account_id = WAW.fetch_accountid(ign)
        wst.add_userid(account_id)
    
        clan_id = WAW.fetch_clan_id(account_id)
        clan_tag = None if clan_id is None else WAW.fetch_clan_tag(clan_id)
        wst.add_clan(clan_tag)
    
        ship_id = vehicle["shipId"]
        wst.add_ship_info(ship_id, SI.tier(ship_id), SI.name(
            ship_id), SI.nation(ship_id), SI.ship_type(ship_id))

        personal_data = WAW.fetch_personal_data(account_id)
        ship_stats, rank_info = None if personal_data is None else WAW.fetch_ship_stats(
            account_id, ship_id), WAW.fetch_rank_stats(account_id)
        wst.add_personal_data(personal_data)
        wst.add_ship_stats(ship_stats)
        wst.add_rank(rank_info)
    
        wst.update_tmplist(vehicle["relation"])
    
    wst.sort_tmplist()
    data = wst.create_stats_dict(ArenaInfo["mapDisplayName"])
    
    return data

APP = Bottle()
SERVER = WSGIServer(("0.0.0.0", 8080), APP, handler_class=WebSocketHandler)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@APP.route('/static/<file_path:path>')
def static(file_path):
    """
    Returning static file when accessing localhost:8080/static/
    """
    return static_file(file_path, root='{}/static'.format(BASE_DIR))

@APP.route('/websocket')
def handle_websocket():
    """
    WebSocket Handler
    Return data once every 5 seconds
    """
    websocket = request.environ.get('wsgi.websocket')
    if not websocket:
        abort(400, 'Expected WebSocket request.')
    
    count = 0
    while True:
        count += 1
        if count % 10 != 0:
            sleep(3)
            continue

        with open("tempArenaInfo.json", "r", encoding="utf-8_sig") as json_file:
            ArenaInfo = load(json_file)

        print(datetime.datetime.now())
        data = test(ArenaInfo)
        print(datetime.datetime.now())
        try:
            handler = websocket.handler
            for client in handler.server.clients.values():
                client.ws.send(dumps(data))

        except WebSocketError:
            break

@APP.route('/')
def top():
    """
    Returning WebSocket client when accessing localhost:8080/
    """
    return static_file('static/index.html', root='./')

SERVER.serve_forever()
