"""ship info"""
import json
import configparser

import wows_api_wrapper


INIFILE = configparser.SafeConfigParser()
INIFILE.read('../config/config.ini', 'UTF-8')
app_id = INIFILE["Config"]["application_id"]
region = INIFILE["Config"]["region"]
WAW = wows_api_wrapper.APIWrapper(app_id=app_id, region=region)


class ShipInfo():
    """
    Class handling ships data
    Include method to get each information from ship id
    """
    def __init__(self):
        """
        ship_dict : dict
            Extract necessary items from all ship data acquired from API
        """
        ship_enc_dict = WAW.fetch_ship_encyclopedia()
        print(type(ship_enc_dict))
        ships_info_dict = {}
        count = 0
        for ship_id, ship_data in ship_enc_dict.items():
            ship_info_dict = {}
            ship_info_dict["name"] = ship_data["name"]
            ship_info_dict["nation"] = ship_data["nation"]
            ship_info_dict["tier"] = ship_data["tier"]
            ship_info_dict["type"] = ship_data["type"]
            ship_info_dict["is_premium"] = ship_data["is_premium"]
            ships_info_dict[ship_id] = ship_info_dict
            count += 1
            print(count)

        ship_enc_dict = {}

        self.ships_info_dict = ships_info_dict

    def dump(self):
        """
        """
        with open("ships_info.json", mode="w", encoding="utf-8_sig") as json_file:
            json.dump(self.ships_info_dict, json_file, ensure_ascii=False, indent=4, \
                      sort_keys=True, separators=(',', ': '))

if __name__ == "__main__":
    SI = ShipInfo()
    SI.dump()