"""Server"""
import os
from datetime import datetime
from time import sleep
from json import load, dumps
from json.decoder import JSONDecodeError

from bottle import route, run, static_file, request, Bottle, abort

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

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

    json_path = "{}/application/data.json".format(BASE_DIR)
    with open(json_path, 'r', encoding="utf-8_sig") as json_file:
        data = load(json_file)

    if not websocket:
        abort(400, 'Expected WebSocket request.')
    count = 0

    while True:
        count += 1
        if count % 10 == 1:
            print(count)
            continue
        try:
            handler = websocket.handler
            for client in handler.server.clients.values():
                client.ws.send(dumps(data))

        except WebSocketError:
            break

        sleep(3)

@APP.route('/')
def top():
    """
    Returning WebSocket client when accessing localhost:8080/
    """
    return static_file('static/index.html', root='./')

SERVER.serve_forever()
