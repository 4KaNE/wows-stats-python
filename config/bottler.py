"""open setting.html"""
from os.path import isdir, isfile
import json
import webbrowser as web
from bottle import route, run, post, template, request
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
    ign : str
    region : str    

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
        print("AAAA")
    else:
        result = False
    print(error_list)

    return result, error_list, account_id



@route('/setting')
def setting():
    return template('setting.tpl', errorMessage="")

@post('/setting')
def do_setting():
    wows_path = request.forms.wowsPath
    app_id = request.forms.appId
    region = request.forms.region
    ign = request.forms.ign
    no_value = template('setting.tpl', errorMessage="全ての欄に入力してください")
    if wows_path == "":
        return no_value
    elif app_id == "":
        return no_value
    elif ign == "":
        return no_value

    wows_path = wows_path.replace("\\", "/")
    result, error_list, account_id = check(wows_path, app_id, ign, region)
    print(result)

    print(account_id)

    error_message = ""
    for error in error_list:
        error_message += "ERROR!: {}\n".format(error)

    if result:
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

