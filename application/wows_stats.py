"""wows stats"""

class WoWsStats():
    """
    Class for storing information to be displayed 
    on the client in json format
    """
    def __init__(self):
        self.stats_dict = {}
        self.friends_stats_list = []
        self.enemy_stats_list = []
