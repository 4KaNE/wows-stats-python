"""test"""
import os
from bottle import route, run, static_file
from bottle import TEMPLATE_PATH, jinja2_template as template

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_DIR = os.path.join(BASE_DIR, 'static')

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
