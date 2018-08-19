"""test"""
import os
from json import load, dump
from json.decoder import JSONDecodeError
from bottle import route, run, static_file
from bottle import TEMPLATE_PATH, jinja2_template as template


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_DIR = os.path.join(BASE_DIR, 'static')

@route('/')
def hoge():
    """
    test
    """
    json_path = "{}/application/data.json".format(BASE_DIR)
    with open(json_path, 'r', encoding="utf-8_sig") as json_file:
        data = load(json_file)
    
    flag = 0

    return template('static/index', data=data, flag=flag)

@route('/static/<file_path:path>')
def static(file_path):
    """css"""
    return static_file(file_path, root='./static')

run(host='localhost', port=8080,  reloader=True, debug=True)
