"""WoWS API warapper"""
import json
import requests

class api_wrapper(app_id, region):
    """
    Class wrapping the WoWS API

    Parameters
    ----------
    app_id : str
        ApplicationId required for calling API
    region : str
        The server region to which the user belongs
    """
    def __init__(self):
        self.app_id = app_id
        self.region = region