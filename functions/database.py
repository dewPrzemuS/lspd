import json
import os

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(
    f"{os.path.dirname(os.path.realpath(__file__))}/special/prl-lspd-firebase-adminsdk-h4h4b-0c8982594e.json")
firebase = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://prl-lspd-default-rtdb.europe-west1.firebasedatabase.app/"
})

main = db.reference("/")

jsonFileData = open(f"{os.path.dirname(os.path.realpath(__file__))}/data.json")
data = json.loads(jsonFileData.read())
