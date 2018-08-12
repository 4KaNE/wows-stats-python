"""open setting.html"""
from os.path import isdir, isfile
import webbrowser as web
from bottle import route, run, post, template, request

web.open('http://localhost:8080/setting')

def check_wows_path(path :str) -> bool:
    """
    Check if the entered path is correct.
    
    Parameters
    ----------
    path : str
        Path of directory where WorldOfWarships.exe is located
    
    Returns
    ----------
    result : bool
        True if path is correct, False otherwise.
    """
    result = False
    exe_path = path + "/WorldOfWarships.exe"
    if isfile(exe_path):
        result = True

    return result


@route('/setting')
def setting():
    return template('setting.tpl', errorMessage="")

@post('/setting')
def do_setting():
    wows_path = request.forms.wowsPath

    app_id = request.forms.appId
    region = request.forms.region
    ign = request.forms.ign
    wows_path = wows_path.replace("\\", "/")
    print(wows_path)
    print(app_id)
    print(region)
    print(ign)

    success = False
    error_list = []
    if not check_wows_path(wows_path):
        error_list.append("入力されたWoWsディレクトリのパスが不正です。")

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

