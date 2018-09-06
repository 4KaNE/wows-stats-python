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
    wst.add_userid(account_id)

    clan_id = WAW.fetch_clan_id(account_id)
    clan_tag = None if clan_id is None else WAW.fetch_clan_tag(clan_id)
    wst.add_clan(clan_tag)

    ship_id = vehicle["shipId"]
    wst.add_ship_info(ship_id, SI.tier(ship_id), SI.name(
        ship_id), SI.nation(ship_id), SI.ship_type(ship_id))

    personal_data = WAW.fetch_personal_data(account_id)
    ship_stats, rank_info = None if personal_data is None else WAW.fetch_ship_stats(
        account_id, ship_id), WAW.fetch_rank_stats(account_id)
    wst.add_personal_data(personal_data)
    wst.add_ship_stats(ship_stats)
    wst.add_rank(rank_info)

    wst.update_tmplist(vehicle["relation"])

wst.sort_tmplist()
print(wst.friends_stats_list)
