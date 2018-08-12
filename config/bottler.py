"""open setting.html"""
import webbrowser as web
from bottle import route, run, post, template, request

web.open('http://localhost:8080/setting')
    
@route('/setting')
def setting():
    return template('setting.tpl', statusMessage="AAA")


@post('/setting')
def do_setting():
    username = request.forms.username
    password = request.forms.password
    print(username)
    print(password)

    return template('setting.tpl', statusMessage="success!")


run(host='localhost', port=8080, debug=True)    