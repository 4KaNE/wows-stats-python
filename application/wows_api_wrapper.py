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

    def api_caller(self, url):
        """
        Fetch data from the API using the received request URL
        If API restriction error returns, retry for up to 5 times

        Parameters
        ----------
        url : str
            URL for API request
        returns
        ----------
        data : dict
            Data returned from the API
            If the request fails, None is returned
        """
        count = 0
        while count < 5:
            count += 1
            try:
                result = requests.get(url)
            except:
                sleep(self.retry)
                data == None
                continue

            data = json.loads(result.text)
            if data["status"] == "error":
                if data["error"]["message"] == "REQUEST_LIMIT_EXCEEDED":
                    print("API制限")
                    sleep(self.retry)
                    continue

            break

        return data
            

    def fetch_accountid(self, ign: str) -> str:
        """
        fetch account id using ign
        
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
        data = self.api_caller(url)
        account_id = None
        if data is None:
            return account_id

        elif data["status"] == "error":
            account_id = None        
        elif data["status"] == "ok":
            if data["meta"]["count"] == 0:
                print("プレイヤーが存在しない")
                account_id = None        
            else:
                account_id = data["data"][0]["account_id"]

        return account_id

