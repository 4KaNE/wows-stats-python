from bottle import route, run
    
@route('/setting')
def hello():
    return "Hello World!"
    
run(host='localhost', port=8080, debug=True)