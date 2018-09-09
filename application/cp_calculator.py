"""CP calculator"""


class CPCalculator():
    """
    Class for calculating fighting strength evaluation value
    """

    def __init__(self):
        pass

    def _calc_combat_power(self, ship_type, damage, kd_ratio, exp, tier):
        """
        Evaluation value used in wows-stats-master
        """
        if ship_type == "CV":
            type_param = 0.5
        elif ship_type == "BB":
            type_param == 0.7
        else:
            type_param == 1.0

        combat_power = damage * kd_ratio * exp / \
            800 * (1 - (0.03 * tier)) * type_param

        return combat_power
