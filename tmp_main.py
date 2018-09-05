"""test wows_stats.py"""
import configparser
import json
from application import wows_api_wrapper, ships_info, wows_stats

INIFILE = configparser.SafeConfigParser()
INIFILE.read('./config/config.ini', 'UTF-8')
app_id = INIFILE["config"]["application_id"]
region = INIFILE["config"]["region"]
SI = ships_info.ShipInfo(app_id, region)
WAW = wows_api_wrapper.APIWrapper(app_id, region)

with open("tempArenaInfo.json", "r", encoding="utf-8_sig") as json_file:
    ArenaInfo = json.load(json_file)

wst = wows_stats.WoWsStats()

for vehicle in ArenaInfo["vehicles"]:
    wst.init_user_dict()
    ign = vehicle["name"]
    wst.add_ign(ign)
    account_id = WAW.fetch_accountid(ign)

    clan_id = WAW.fetch_clan_id(account_id)
    clan_tag = WAW.fetch_clan_tag(clan_id)
    wst.add_clan(clan_tag)

    ship_id = vehicle["shipId"]
    wst.add_tier(SI.tier(ship_id))
    wst.add_ship_name(SI.name(ship_id))
    wst.add_ship_nationality(SI.nation(ship_id))
    wst.add_ship_class(SI.ship_type(ship_id))

    print(wst.user_dict)
