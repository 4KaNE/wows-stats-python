"""CP calculator"""


class CPCalculator():
    """
    Class for calculating fighting strength evaluation value
    """

    def __init__(self):
        pass

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
