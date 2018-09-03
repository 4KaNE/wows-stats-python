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

    def add_before_rank(self, before_rank):
        self.user_dict["before_rank"] = before_rank

    def add_now_rank(self, now_rank):
        self.user_dict["now_rank"] = now_rank

    def add_ship_name(self, ship_name):
        self.user_dict["ship_name"] = ship_name
    
    def add_tier(self, tier):
        self.user_dict["tier"] = tier

    def add_ship_wr(self, ship_wr):
        self.user_dict["ship_wr"] = ship_wr

    def add_ship_class(self, ship_class):
        self.user_dict["ship_class"] = ship_class

    def add_ship_nationality(self, ship_nationality):
        self.user_dict["ship_nationality"] = ship_nationality

    def add_shipexp(self, ship_exp):
        self.user_dict["ship_exp"] = ship_exp

    def add_kill_death(self, kill_death):
        self.user_dict["kill_death"] = kill_death

    def add_shot_down(self, shot_down):
        self.user_dict["shot_down"] = shot_down

    def add_winning_survive(self, winning_survive):
        self.user_dict["winning_survive"] = winning_survive

    def add_losing_survive(self, losing_survive):
        self.user_dict["losing_survive"] = losing_survive

if __name__ == "__main__":
    WWS = WoWsStats()
    WWS.hoge()
    WWS.test()
    WWS.hoge()
    WWS.__init__()
    WWS.hoge
