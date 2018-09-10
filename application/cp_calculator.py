"""CP calculator"""
import requests
import ast
from json import dump


class CPCalculator():
    """
    Class for calculating fighting strength evaluation value
    """

    def __init__(self):
        pr_data = requests.get(
            "https://asia.wows-numbers.com/personal/rating/expected/json/")
        self.pr_dict = ast.literal_eval(pr_data.text)

    def combat_power(self, player_stats):
        """
        Handle combat power calculation
        """
        damage = player_stats["damage"]
        damage = damage if type(damage) in (int, float) else 0
        kd_ratio = player_stats["kill_death"]
        kd_ratio = kd_ratio if type(kd_ratio) in (int, float) else 0
        exp = player_stats["ship_exp"]
        exp = exp if type(kd_ratio) in (int, float) else 0
        tier = player_stats["tier"]
        tier = tier if type(kd_ratio) in (int, float) else 0
        result = self._calc_combat_power(
            player_stats["ship_class"], damage, kd_ratio, exp, tier
        )
        return result

    def _calc_combat_power(self, ship_type, damage, kd_ratio, exp, tier):
        """
        Evaluation value used in wows-stats-master
        """
        if ship_type == "CV":
            type_param = 0.5
        elif ship_type == "BB":
            type_param = 0.7
        else:
            type_param = 1.0

        combat_power = damage * kd_ratio * exp / \
            800 * (1 - (0.03 * tier)) * type_param
        combat_power = round(combat_power)

        return combat_power

    def personal_rating(self, player_stats):
        """
        Handle personal rating calculation
        """
        damage = player_stats["damage"]
        damage = damage if type(damage) in (int, float) else 0
        wins = player_stats["ship_wr"]
        wins = wins if type(wins) in (int, float) else 0
        kill_ratio = player_stats["kill_ratio"]
        kill_ratio = kill_ratio if type(kill_ratio) in (int, float) else 0

        result = self._calc_personal_rating(player_stats["ship_id"], damage, wins, kill_ratio)
        return result

    def _calc_personal_rating(self, ship_id, actual_dmg, actual_wins, actual_frags):
        """
        Evaluation value used in WoWS Stats & Numbers
        """
        r_dmg = actual_dmg / self.pr_dict["data"][str(ship_id)]["average_damage_dealt"]
        r_wins = actual_wins / self.pr_dict["data"][str(ship_id)]["win_rate"]
        r_frags = actual_frags / self.pr_dict["data"][str(ship_id)]["average_frags"]

        n_dmg = max(0, (r_dmg - 0.4) / (1 - 0.4))
        n_frags = max(0, (r_wins - 0.1) / (1 - 0.1))
        n_wins = max(0, (r_frags - 0.7) / (1 - 0.7))

        pr =  700 * n_dmg + 300 * n_frags + 150 * n_wins
        result = round(pr)
        return result

if __name__ == '__main__':
    CPC = CPCalculator()
    player_stats = {
        "damage": 61757,
        "kill_ratio": 1.07,
        "ship_wr": 64.17,
        "ship_id": 4282365648
    }
    print(CPC.personal_rating(player_stats))