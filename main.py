"""test"""
import os
from datetime import datetime
from time import sleep
from json import load, dumps
from json.decoder import JSONDecodeError

from bottle import route, run, static_file, request, Bottle, abort
from bottle import TEMPLATE_PATH, jinja2_template as template

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

APP = Bottle()
SERVER = WSGIServer(("0.0.0.0", 8080), APP, handler_class=WebSocketHandler)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_DIR = os.path.join(BASE_DIR, 'static')

"""
@route('/')
def hoge():
    json_path = "{}/application/data.json".format(BASE_DIR)
    with open(json_path, 'r', encoding="utf-8_sig") as json_file:
        data = load(json_file)
    
    flag = 1

    return template('static/index', data=data, flag=flag)
"""

@route('/static/<file_path:path>')
def static(file_path):
    """css"""
    print("AAAAAAAA")
    return static_file(file_path, root='{}/static'.format(BASE_DIR))

@APP.route('/websocket')
def handle_websocket():
    """
    WebSocket Handler
    Return count once every 3 seconds
    """
    websocket = request.environ.get('wsgi.websocket')

    json_path = "{}/application/data.json".format(BASE_DIR)
    with open(json_path, 'r', encoding="utf-8_sig") as json_file:
        data = load(json_file)

    if not websocket:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            handler = websocket.handler
            for client in handler.server.clients.values():
                now_time = datetime.strftime(datetime.now(), '%H:%M:%S')
                print(now_time)
                client.ws.send(dumps(data))

        except WebSocketError:
            break

        sleep(10)

@APP.route('/')
def top():
    """
    Returning WebSocket client when accessing localhost:8080/
    """
    return static_file('static/index.html', root='./')

SERVER.serve_forever()

#run(host='localhost', port=8080,  reloader=True, debug=True)
