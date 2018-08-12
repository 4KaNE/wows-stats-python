"""open setting.html"""
import webbrowser as web
from bottle import route, run, post, request

web.open('http://localhost:8080/setting')
    
@route('/setting')
def setting():
    return """
    <form action="/setting" method="post">
    Username: <input name="username" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
    </form>
    """

@post('/setting')
def do_setting():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username)
    print(password)

    return "success!"

    
run(host='localhost', port=8080, debug=True)