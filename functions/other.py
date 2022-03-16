import json
import os

from flask import request

jsonFileData = open(f"{os.path.dirname(os.path.realpath(__file__))}/data.json")
data = json.loads(jsonFileData.read())


def getIP():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return str(request.environ['REMOTE_ADDR'])
    else:
        return str(request.environ['HTTP_X_FORWARDED_FOR'])
