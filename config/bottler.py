"""open setting.html"""
import webbrowser as web
from bottle import route, run, post, template, request

web.open('http://localhost:8080/setting')
    
@route('/setting')
def setting():
    return template('setting.tpl', errorMessage="")

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

    success = False
    error = "存在しないアプリケーションキーです"
    error_message = "ERROR!: {}".format(error)

    if success:
        return """
            <html>
            <head>
              <style type='text/css'>
                body {
                  background-color: #36393f;
                  color: #DCDDDE;
                  text-align: center;
                }
                h3 {
                    color: #EEA34A
                }
              </style>
            
            </head>
            <body>
              <h3>成功</h3>
              登録完了しました!<br>
              run.batで起動することができます。<br>
            </body>
            </html>"""

    else:
        return template('setting.tpl', errorMessage=error_message)


run(host='localhost', port=8080, debug=True)