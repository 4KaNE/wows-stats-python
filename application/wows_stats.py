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
        self.tmp_friends_stats_list = []
        self.tmp_enemy_stats_list = []
        self.user_dict = {}
        self.before_season = 9
        self.now_season = 10
        self.no_data = "--"

    def test(self):
        self.user_dict["test"] = "aaa"

    def hoge(self):
        print(self.user_dict)

    def init_user_dict(self):
        self.user_dict = {
            "before_rank": 0,
            "clan": "",
            "combat_power_1": 0,
            "combat_power_2": 0,
            "damage": 0,
            "ign": "",
            "kill_death": 0.0,
            "losing_survive": 0,
            "myself_flag": 0,
            "now_rank": 0,
            "overall_battle_number": 0,
            "overall_exp": 0,
            "overall_wr": 0.0,
            "ship_battle_number": 0,
            "ship_class": "",
            "ship_exp": 0,
            "ship_name": "",
            "ship_nationality": "",
            "ship_wr": 0.0,
            "shot_down": 0.0,
            "tier": 0,
            "winning_survive": 0
        }
    
    def add_ign(self, ign):
        self.user_dict["ign"] = ign

    def add_clan(self, clan):
        clan = self.no_data if clan is None else clan
        self.user_dict["clan"] = clan

    def add_combat_power(self, combat_power, num):
        self.user_dict["combat_power{}".format(num)] = combat_power

    def add_personal_data(self, personal_data):
        if personal_data is None:
            self.user_dict["overall_battle_number"] = self.no_data
            self.user_dict["overall_wr"] = self.no_data
            self.user_dict["overall_exp"] = self.no_data
        else:
            battles = personal_data["statistics"]["pvp"]["battles"]
            self.user_dict["overall_battle_number"] = battles
            wins = personal_data["statistics"]["pvp"]["wins"]
            self.user_dict["overall_wr"] = round(wins / battles, 3) *100
            exp = personal_data["statistics"]["pvp"]["exp"]
            self.user_dict["overall_exp"] = exp // battles

    def add_rank(self, rank_stats):
        if rank_stats is None:
            self.user_dict["before_rank"] = "**"
            self.user_dict["now_rank"] = "**"
        else:
            before_rank = rank_stats["seasons"][str(self.before_season)]\
                                    ["rank_info"]["max_rank"]
            before_rank = "**" if before_rank == 0 else before_rank
            self.user_dict["before_rank"] = before_rank
            now_rank = rank_stats["seasons"][str(self.now_season)]\
                                    ["rank_info"]["rank"]
            now_rank = "**" if now_rank == 0 else now_rank
            self.user_dict["now_rank"] = now_rank

    def add_ship_stats(self, ship_stats):
        if ship_stats is None:
            self.user_dict["damage"] = self.no_data
            self.user_dict["kill_death"] = self.no_data
            self.user_dict["ship_wr"] = self.no_data
            self.user_dict["shot_down"] = self.no_data
            self.user_dict["winning_survive"] = self.no_data
            self.user_dict["losing_survive"] = self.no_data
            self.user_dict["ship_exp"] = self.no_data
            self.user_dict["ship_battle_number"] = self.no_data
        else:
            battles = ship_stats["pvp"]["battles"]
            self.user_dict["ship_battle_number"] = battles
            damage = ship_stats["pvp"]["damage_dealt"]
            self.user_dict["damage"] = damage // battles
            survive = ship_stats["pvp"]["survived_battles"]
            frags = ship_stats["pvp"]["frags"]
            self.user_dict["kill_death"] = round(frags / (battles - survive), 3) * 100
            wins = ship_stats["pvp"]["wins"]
            self.user_dict["ship_wr"] = round(wins / battles, 3) * 100
            planes_killed = ship_stats["pvp"]["planes_killed"]
            self.user_dict["shot_down"] = round(planes_killed / battles, 1)
            survived_wins = ship_stats["pvp"]["survived_wins"]
            self.user_dict["winning_survive"] = survived_wins // battles
            survived_battles = ship_stats["pvp"]["survived_battles"]
            self.user_dict["losing_survived"] = (survived_battles -survived_wins) // battles
            exp = ship_stats["pvp"]["xp"]
            self.user_dict["ship_exp"] = exp // battles


    def add_ship_name(self, ship_name):
        self.user_dict["ship_name"] = ship_name
    
    def add_tier(self, tier):
        self.user_dict["tier"] = tier

    def add_ship_class(self, ship_class):
        self.user_dict["ship_class"] = ship_class

    def add_ship_nationality(self, ship_nationality):
        self.user_dict["ship_nationality"] = ship_nationality


if __name__ == "__main__":
    WWS = WoWsStats()
    WWS.hoge()
    WWS.test()
    WWS.hoge()
    WWS.__init__()
    WWS.hoge
