import json
import os

from flask import request

jsonFileData = open(f"{os.path.dirname(os.path.realpath(__file__))}/data.json")
data = json.loads(jsonFileData.read())
