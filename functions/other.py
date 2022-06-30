import json
import os

from flask import request

jsonFileData = open(f"{os.path.dirname(os.path.realpath(__file__))}/data.json", "r", encoding="utf8")
data = json.loads(jsonFileData.read())