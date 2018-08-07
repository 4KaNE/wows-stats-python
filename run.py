"""test"""
import os
from bottle import route, run, template, static_file


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

@route('/')
def hoge():
    """
    test
    """
    return template('static/index', test="Hello bottle!")

@route('/static/<file_path:path>')
def static(file_path):
    """css"""
    return static_file(file_path, root='./static')

run(host='localhost', port=8080,  reloader=True, debug=True)
