"""open setting.html"""
import webbrowser as web
from bottle import route, run, post, template, request

web.open('http://localhost:8080/setting')
    
@route('/setting')
def setting():
    return template('setting.tpl', statusMessage="")

@post('/setting')
def do_setting():
    wows_path = request.forms.wowsPath
    app_id = request.forms.appId
    region = request.forms.region
    ign = request.forms.ign
    print(wows_path)
    print(app_id)
    print(region)
    print(ign)

    return template('setting.tpl', statusMessage="success!")


run(host='localhost', port=8080, debug=True)