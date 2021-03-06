"""wows stats"""
from operator import itemgetter


class WoWsStats():
    """
    Class for storing information to be displayed 
    on the client in json format
    """

    def __init__(self):
        self.stats_dict = {}
        self.friends_list = []
        self.enemies_list = []
        self.user_dict = {}
        self.before_season = 9
        self.now_season = 10
        self.no_data = "--"

    def create_stats_dict(self, map_name):
        stats_dict = {}
        stats_dict["friends"] = self.friends_list
        stats_dict["enemies"] = self.enemies_list
        stats_dict["map_name"] = map_name
        return stats_dict

    def init_user_dict(self):
        self.user_dict = {
            "before_rank": 0,
            "clan": "",
            "combat_power_1": 0,
            "combat_power_2": 0,
            "damage": 0,
            "ign": "",
            "kill_death": 0.0,
            "kill_ratio": 0.0,
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
            "winning_survive": 0,
            "user_id": 0,
            "ship_id": 0
        }

    def add_userid(self, user_id):
        user_id = 0 if user_id is None else user_id
        self.user_dict["user_id"] = user_id

    def add_ship_id(self, ship_id):
        self.user_dict["ship_id"] = ship_id

    def add_ign(self, ign):
        self.user_dict["ign"] = ign

    def add_clan(self, clan):
        clan = self.no_data if clan is None else clan
        self.user_dict["clan"] = clan

    def add_combat_power(self, combat_power, num):
        self.user_dict["combat_power_{}".format(num)] = combat_power

    def add_personal_data(self, personal_data):
        if personal_data is None:
            self.user_dict["overall_battle_number"] = self.no_data
            self.user_dict["overall_wr"] = self.no_data
            self.user_dict["overall_exp"] = self.no_data
        else:
            battles = personal_data["statistics"]["pvp"]["battles"]
            self.user_dict["overall_battle_number"] = battles
            wins = personal_data["statistics"]["pvp"]["wins"]
            self.user_dict["overall_wr"] = round(
                self._division(wins, battles)*100, 1)
            exp = personal_data["statistics"]["pvp"]["xp"]
            self.user_dict["overall_exp"] = self._division(exp, battles, True)

    def add_rank(self, rank_stats):
        if rank_stats is None:
            self.user_dict["before_rank"] = "**"
            self.user_dict["now_rank"] = "**"
        else:
            before_season_stats = rank_stats["seasons"].get(
                str(self.before_season))
            before_rank = before_season_stats["rank_info"]["max_rank"] \
                if before_season_stats is not None else None
            before_rank = "**" if before_rank == 0 else before_rank
            self.user_dict["before_rank"] = before_rank
            now_rank = rank_stats["seasons"][str(
                self.now_season)]["rank_info"]["rank"]
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
            battles = ship_stats["battles"]
            self.user_dict["ship_battle_number"] = battles
            damage = ship_stats["damage_dealt"]
            self.user_dict["damage"] = self._division(damage, battles, True)
            survive = ship_stats["survived_battles"]
            frags = ship_stats["frags"]
            self.user_dict["kill_death"] = round(
                self._division(frags, (battles - survive)), 1)
            self.user_dict["kill_ratio"] = round(
                self._division(frags, battles), 2)
            wins = ship_stats["wins"]
            self.user_dict["ship_wr"] = round(
                self._division(wins, battles)*100, 1)
            planes_killed = ship_stats["planes_killed"]
            self.user_dict["shot_down"] = round(
                self._division(planes_killed, battles), 1)
            survived_wins = ship_stats["survived_wins"]
            self.user_dict["winning_survive"] = self._division(
                survived_wins*100, wins, True)
            survived_battles = ship_stats["survived_battles"]
            self.user_dict["losing_survive"] = self._division(
                (survived_battles - survived_wins)*100, (battles - wins), True)
            exp = ship_stats["xp"]
            self.user_dict["ship_exp"] = self._division(exp, battles, True)

    def add_ship_info(self, ship_id, tier, ship_name, nation, ship_class):
        self.add_ship_id(ship_id)
        self.add_tier(tier)
        self.add_ship_name(ship_name)
        self.add_ship_nationality(nation)
        self.add_ship_class(ship_class)

    def add_ship_name(self, ship_name):
        self.user_dict["ship_name"] = ship_name

    def add_tier(self, tier):
        self.user_dict["tier"] = tier

    def add_ship_class(self, ship_class):
        class_dict = {
            "AirCarrier": "CV",
            "Battleship": "BB",
            "Cruiser": "CA/CL",
            "Destroyer": "DD"
        }
        self.user_dict["ship_class"] = class_dict.get(ship_class)

    def add_ship_nationality(self, ship_nationality):
        self.user_dict["ship_nationality"] = ship_nationality

    def update_tmplist(self, relation):
        if relation == 0 or relation == 1:
            self.friends_list.append(self.user_dict)
        else:
            self.enemies_list.append(self.user_dict)

    def sort_tmplist(self):
        for tmp_list in [self.friends_list, self.enemies_list]:
            tmp_list.sort(key=itemgetter("user_id"))
            tmp_list.sort(key=itemgetter("ship_id"))
            tmp_list.sort(key=self._sort_nation)
            tmp_list.sort(key=itemgetter("tier"), reverse=True)
            tmp_list.sort(key=self._sort_ship_type)

    def _sort_ship_type(self, tmp_userdict):
        ship_type = tmp_userdict["ship_class"]
        sort_dict = {
            "CV": 1,
            "BB": 2,
            "CA/CL": 3,
            "DD": 4
        }
        return sort_dict.get(ship_type, 5)

    def _sort_nation(self, tmp_userdict):
        """
        Receive nation and return the corresponding order as int
        """
        nation = tmp_userdict["ship_nationality"]
        order_dict = {
            "usa": 1,
            "japan": 2,
            "ussr": 3,
            "germany": 4,
            "uk": 5,
            "poland": 6,
            "pan_asia": 7,
            "france": 8,
            "italy": 9,
            "commonwealth": 10,
            "pan_america": 11
        }
        return order_dict.get(nation, 12)

    def _division(self, num, denom, trunc=False):
        if trunc:
            try:
                result = num // denom
            except ZeroDivisionError:
                result = 0
        else:
            try:
                result = num / denom
            except ZeroDivisionError:
                result = 0

        return result
