"""open setting.html"""
from os.path import isdir, isfile
import json
import webbrowser as web
from bottle import route, run, post, template, request, get, static_file
import requests


web.open('http://localhost:8080/setting')

def check(path: str, app_id: str, ign: str, region: str):
    """
    Check if the entered value is correct.

    Parameters
    ----------
    path : str
        Path of directory where WorldOfWarships.exe is located.
    app_id : str
        Application key for accessing wows API
    ign : str
        Name in your game
    region : str
        The server region you are playing

    Returns
    ----------
    result : bool
    error_list : list
    """
    result = False
    error_list = []
    account_id = None

    exe_path = path + "/WorldOfWarships.exe"
    if not isfile(exe_path):
        error_list.append("入力されたWoWsディレクトリのパスが不正です。")

    api = "https://api.worldofwarships.{region}/wows/account/list/\
            ?application_id={application_id}&search={search}"
    url = api.format(region=region, application_id=app_id, search=ign)
    result = requests.get(url)
    data = json.loads(result.text)
    if data["status"] == "error":
        if data["error"]["message"] == "INVALID_APPLICATION_ID":
            error_list.append("入力されたアプリケーションIDは無効です")
        elif data["error"]["message"] == "INVALID_SEARCH":
            error_list.append("入力されたIGNは無効です")
    
    elif data["status"] == "ok":
        if data["meta"]["count"] == 0:
            error_list.append("存在しないIGNです")
        elif data["meta"]["count"] == 1:
            account_id = data["data"][0]["account_id"]
        else:
            if data["data"][0]["nickname"] == ign:
                account_id = data["data"][0]["account_id"]
            else:
                error_list.append("複数のIGNがヒットしました。IGNはフルで入力してください")

    if len(error_list) == 0:
        result = True
    else:
        result = False

    return result, error_list, account_id

def save_config(path: str, app_id: str, account_id: str, region: str):
    """
    Save config in ini file.
    
    Parameters
    ----------
    path : str
        Path of directory where WorldOfWarships.exe is located.
    app_id : str
        Application key for accessing wows API
    account_id : str
        Your account id on wows
    region : str
        The server region you are playing
    """
    config = """[config]
wows_path : {}
application_id : {}
account_id : {}
region : {}""".format(path, app_id, account_id, region)
    print(config)
    with open('config.ini', 'w', encoding="utf-8") as ini_file:
        ini_file.write(config)

@route('/static/<file_path:path>')
def static(file_path):
    """
    Returning static file when accessing localhost:8080/static/
    """
    return static_file(file_path, root='../static')

@route('/setting')
def setting():
    return template('setting.html', errorMessage="")

@post('/setting')
def do_setting():
    wows_path = request.forms.wowsPath
    app_id = request.forms.appId
    region = request.forms.region
    ign = request.forms.ign
    no_value = template('setting.html', errorMessage="全ての欄に入力してください")
    if wows_path == "" or app_id == "" or ign == "":
        return no_value

    wows_path = wows_path.replace("\\", "/")
    result, error_list, account_id = check(wows_path, app_id, ign, region)

    if result:
        save_config(wows_path, app_id, account_id, region)
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
    
    error_message = ""
    for error in error_list:
        error_message += "ERROR!: {}\n".format(error)

    else:
        return template('setting.html', errorMessage=error_message)


run(host='localhost', port=8080, debug=True)

