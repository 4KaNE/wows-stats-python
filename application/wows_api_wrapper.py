"""WoWS API warapper"""
import json
import requests
from time import sleep

class APIWrapper():
    """
    Class wrapping the WoWS API

    Parameters
    ----------
    app_id : str
        ApplicationId required for calling API
    region : str
        The server region to which the user belongs
    """
    def __init__(self, app_id, region):
        self.app_id = app_id
        self.region = region
        self.retry = 0.1

    def fetch_accountid(self, ign: str) -> str:
        """
        fetch account id using ign
        If API restriction error returns, retry for up to 5 times

        Parameters
        ----------
        ign : str
            user's IGN

        returns
        ----------
        account_id : str
            user's account id
            If IGN does not exist or if some error occurs, None is returned
        """
        api = "https://api.worldofwarships.{region}/wows/account/list/\
               ?application_id={application_id}&search={ign}"
        url = api.format(region=self.region, application_id=self.app_id,\
                         ign=ign)
        result = requests.get(url)
        data = json.loads(result.text)
        account_id = None
        count = 0
        while count < 5:
            count += 1
            if data["status"] == "error":
                print("エラー")
                if data["error"]["message"] == "REQUEST_LIMIT_EXCEEDED":
                    print("API制限")
                    sleep(self.retry)
                    continue
                else:
                    account_id = None
                    break

            elif data["meta"]["count"] == 0:
                print("プレイヤーが存在しない")
                account_id = None
                break

            elif data["status"] == "ok":
                account_id = data["data"][0]["account_id"]
                break

        return account_id
