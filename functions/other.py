import json
import os

jsonFileLspdData = open(f"{os.path.dirname(os.path.realpath(__file__))}/lspdData.json", "r", encoding="utf8")
dataLspd = json.loads(jsonFileLspdData.read())

jsonFileSupportData = open(f"{os.path.dirname(os.path.realpath(__file__))}/supportData.json", "r", encoding="utf8")
dataSupport = json.loads(jsonFileSupportData.read())


def getalnum(string):
    alphanumeric = [character for character in string if character.isalnum()]
    return "".join(alphanumeric)
