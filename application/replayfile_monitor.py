"""replayfile_monitor"""
from os import path
from json import load, JSONDecodeError


class ReplayFileMonitor():
    """
    Classes that monitor replay file folders
    """

    def __init__(self, wows_path):
        self.replays_path = path.join(wows_path, "replays")
        self.arenainfo = path.join(self.replays_path, "tempArenaInfo.json")
        self.flag = False

    def check_arenainfo(self):
        change = False
        if path.exists(self.arenainfo):
            if not self.flag:
                self.flag = True
                change = True

        else:
            self.flag = False

        return change

    def open_arenainfo(self):
        try:
            with open(self.arenainfo, "r", encoding="utf-8_sig") as json_file:
                try:
                    data = load(json_file)
                except JSONDecodeError:
                    data = None
        except IOError:
            data = None

        return data
