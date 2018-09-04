"""test wows_stats.py"""
import configparser
import json
from application import wows_api_wrapper as WAW
from application import ships_info
from application import wows_stats as WST

INIFILE = configparser.SafeConfigParser()
INIFILE.read('./config/config.ini', 'UTF-8')
app_id = INIFILE["config"]["application_id"]
region = INIFILE["config"]["region"]
SI = ships_info.ShipInfo(app_id, region)

with open("tempArenaInfo.json", "r", encoding="utf-8_sig") as json_file:
    ArenaInfo = json.load(json_file)

for vehicle in ArenaInfo["vehicles"]:
    print(vehicle["name"])
    print(vehicle["shipId"])
    print(SI.name(vehicle["shipId"]))
