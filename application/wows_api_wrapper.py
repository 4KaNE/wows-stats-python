"""WoWS API warapper"""
import json
import requests
from time import sleep
import configparser
import datetime


class APIWrapper():
    """
    Class wrapping the WoWS API
    """

    def __init__(self, app_id, region):
        """
        app_id : str
            Application id for calling API
        region : str
            The server region to which the user belongs
            Any one of [asia, na, eu, ru]
        retry : int of float
            Number of seconds to wait when retrying API call
            The default is 0.1 seconds
        """
        self.app_id = app_id
        self.region = region

    def _api_caller(self, url):
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
        data = None
        count = 0
        while count < 5:
            count += 1
            try:
                result = requests.get(url)
            except:
                continue

            data = json.loads(result.text)
            if data["status"] == "error":
                if data["error"]["message"] == "REQUEST_LIMIT_EXCEEDED":
                    continue

            break

        return data

    def fetch_ship_encyclopedia(self):
        """
        fetch ship data from wows encyclopedia api

        returns
        ----------
        ship_data : dict
            All warship data acquired from API
            It is better to extract only necessary data when using it 
        """
        ship_data = {}
        count = 0
        while True:
            count += 1
            api = "https://api.worldofwarships.{region}/wows/encyclopedia/ships/\
                    ?application_id={app_id}&page_no={page}"
            url = api.format(region=self.region,
                             app_id=self.app_id, page=count)
            data = self._api_caller(url)
            if data["status"] == "error":
                break
            ship_data.update(data["data"])

        return ship_data

    def fetch_accountid(self, ign):
        """
        fetch account id using ign

        Parameters
        ----------
        ign : str
            user's IGN

        returns
        ----------
        account_id : int
            user's account id
            If IGN does not exist or if some error occurs, None is returned
        """
        api = "https://api.worldofwarships.{region}/wows/account/list/\
               ?application_id={app_id}&search={ign}"
        url = api.format(region=self.region, app_id=self.app_id, ign=ign)
        data = self._api_caller(url)
        account_id = None
        if data is None:
            return account_id

        elif data["status"] == "error":
            account_id = None
        elif data["status"] == "ok":
            if data["meta"]["count"] == 0:
                account_id = None
            else:
                account_id = data["data"][0]["account_id"]

        return account_id

    def fetch_clan_id(self, account_id):
        """
        fetch clan id useing account_id

        Parameters
        ----------
        account_id : int or str
            Player's account id

        Results
        ----------
        clan_id : int or 
            Clan id to which the user belongs
            Returns None if data can not be obtained,
            if performance records are not disclosed
            or if user doesn't belongs clan
        """
        api = "https://api.worldofwarships.{region}/wows/clans/accountinfo/\
                ?application_id={app_id}&account_id={account_id}"
        url = api.format(region=self.region,
                         app_id=self.app_id, account_id=account_id)
        data = self._api_caller(url)

        clan_id = None

        if data is None:
            pass
        elif data["status"] != "ok":
            pass
        else:
            if data["data"][str(account_id)] is None:
                clan_id = None
            else:
                clan_id = data["data"][str(account_id)]["clan_id"]

        return clan_id

    def fetch_clan_tag(self, clan_id):
        """
        fetch clan id useing account_id

        Parameters
        ----------
        account_id : int or str
            Player's account id

        Results
        ----------
        clan_id : str
            Clan name
            If some error occurs, None is returned
        """
        api = "https://api.worldofwarships.{region}/wows/clans/info/\
                ?application_id={app_id}&clan_id={clan_id}"
        url = api.format(region=self.region,
                         app_id=self.app_id, clan_id=clan_id)
        data = self._api_caller(url)

        clan_tag = None

        if data is None:
            pass
        elif data["status"] != "ok":
            pass
        else:
            if data["data"][str(clan_id)] is None:
                clan_tag = None
            else:
                clan_tag = data["data"][str(clan_id)]["tag"]

        return clan_tag

    def fetch_personal_data(self, account_id):
        """
        fetch player personal data using account id

        Parameters
        ----------
        account_id : int or str
            Player's account id

        Results
        ----------
        data : dict
            Competitive achievements of players.
            Returns None if data can not be obtained 
            or if performance records are not disclosed
        """
        api = "https://api.worldofwarships.{region}/wows/account/info/\
               ?application_id={app_id}&account_id={account_id}"
        url = api.format(region=self.region,
                         app_id=self.app_id, account_id=account_id)
        data = self._api_caller(url)

        if data is None:
            pass
        elif data["status"] != "ok":
            data = None
        elif data["meta"]["hidden"] is not None:
            data = None
        else:
            data = data["data"][str(account_id)]

        return data

    def fetch_rank_stats(self, account_id):
        """
        fetch player's statistics in ranked battles

        Parameters
        ----------
        account_id : int or str
            Player's account id

        Results
        ----------
        data : dict
            Ranked battle achievements of players.
            Returns None if data can not be obtained 
            or if performance records are not disclosed
        """
        api = "https://api.worldofwarships.{region}/wows/seasons/accountinfo/\
               ?application_id={app_id}&account_id={account_id}"
        url = api.format(region=self.region,
                         app_id=self.app_id, account_id=account_id)
        data = self._api_caller(url)

        if data is None:
            pass
        elif data["status"] != "ok":
            data = None
        elif data["meta"]["hidden"] is not None:
            data = None
        else:
            data = data["data"][str(account_id)]

        return data

    def fetch_ship_stats(self, account_id, ship_id):
        """
        fetch statistics of player's ships

        Parameters
        ----------
        account_id : int or str
            Player's account id
        ship_id : int or str
            Player's ship id

        Results
        ----------
        data : dict
            statistics of player's ships.
            Returns None if data can not be obtained 
            or if performance records are not disclosed
        """
        api = "https://api.worldofwarships.{region}/wows/ships/stats/\
                ?application_id={app_id}&ship_id={ship_id}&account_id={account_id}"
        url = api.format(region=self.region, app_id=self.app_id,
                         ship_id=ship_id, account_id=account_id)
        data = self._api_caller(url)

        if data is None:
            pass
        elif data["status"] != "ok":
            data = None
        elif data["meta"]["hidden"] is not None:
            data = None
        else:
            data = data["data"][str(account_id)][0].get("pvp")

        return data
