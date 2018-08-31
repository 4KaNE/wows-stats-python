"""ship info"""
import json
import configparser

import wows_api_wrapper


class ShipInfo():
    """
    Class handling ships data
    Include method to get each information from ship id
    """
    def __init__(self, app_id, region):
        """
        ship_dict : dict
            Extract necessary items from all ship data acquired from API
        """
        waw = wows_api_wrapper.APIWrapper(app_id=app_id, region=region)
        ship_enc_dict = waw.fetch_ship_encyclopedia()
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

        ship_enc_dict = {}
        print("Acquired {} ships information".format(count))

        self.ships_info_dict = ships_info_dict
    
    def name(self, ship_id):
        """
        """
        ship_info = self.ships_info_dict.get(str(ship_id))
        if ship_info is None:
            name = None
        else:
            name = ship_info["name"]
        
        return name
    
    def nation(self, ship_id):
        """
        """
        ship_info = self.ships_info_dict.get(str(ship_id))
        if ship_info is None:
            nation = None
        else:
            nation = ship_info["nation"]
        
        return nation

    def tier(self, ship_id):
        """
        """
        ship_info = self.ships_info_dict.get(str(ship_id))
        if ship_info is None:
            tier = None
        else:
            tier = ship_info["tier"]
        
        return tier

    def ship_type(self, ship_id):
        """
        """
        ship_info = self.ships_info_dict.get(str(ship_id))
        if ship_info is None:
            ship_type = None
        else:
            ship_type = ship_info["type"]
        
        return ship_type

    def is_premium(self, ship_id):
        """
        """
        ship_info = self.ships_info_dict.get(str(ship_id))
        if ship_info is None:
            is_premium = False
        else:
            is_premium = ship_info["is_premium"]
        
        return is_premium


    def dump(self):
        """
        Output all information to json file
        """
        with open("ships_info.json", mode="w", encoding="utf-8_sig") as json_file:
            json.dump(self.ships_info_dict, json_file, ensure_ascii=False, indent=4, \
                      sort_keys=True, separators=(',', ': '))

if __name__ == "__main__":
    INIFILE = configparser.SafeConfigParser()
    INIFILE.read('../config/config.ini', 'UTF-8')
    app_id = INIFILE["Config"]["application_id"]
    region = INIFILE["Config"]["region"]
    SI = ShipInfo(app_id, region)
    #SI.dump()
    print(SI.name(3335501808))
    print(SI.nation(3335501808))
    print(SI.tier(3335501808))
    print(SI.ship_type(3335501808))
    print(SI.is_premium(3335501808))