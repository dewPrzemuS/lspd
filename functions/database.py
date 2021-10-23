import json
import os

import sshtunnel

sshtunnel.SSH_TIMEOUT = 15.0
sshtunnel.TUNNEL_TIMEOUT = 15.0
import mysql.connector

jsonFileMySQL = open(f"{os.path.dirname(os.path.realpath(__file__))}/special/mysql.json")
sql = json.loads(jsonFileMySQL.read())

jsonFileSSH = open(f"{os.path.dirname(os.path.realpath(__file__))}/special/ssh.json")
ssh = json.loads(jsonFileSSH.read())

with sshtunnel.SSHTunnelForwarder(
        ("ssh.eu.pythonanywhere.com"),
        ssh_username=ssh["username"],
        ssh_password=ssh["password"],
        remote_bind_address=(sql["host"], 3306)
) as server:
    db = mysql.connector.connect(
        host=sql["host"],
        user="uefh3c1k7ynedfai",
        password=sql["password"],
        database="b2wphrwtexyixckyex1x"
    )

    cursor = db.cursor()


    def addEnter(ip, date, method):
        sql = "INSERT INTO entries (ip, date, method) VALUES (%s, %s, %s)"
        val = (ip, date, method)
        cursor.execute(sql, val)
        db.commit()


    def addPenalty(ip, date, range, selected):
        sql = "INSERT INTO penalties (ip, date, penaltyRange, selected) VALUES (%s, %s, %s, %s)"
        val = (ip, date, range, selected)
        cursor.execute(sql, val)
        db.commit()


    def getPenalties():
        sql = "SELECT penaltyRange FROM penalties"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

jsonFileData = open(f"{os.path.dirname(os.path.realpath(__file__))}/data.json")
data = json.loads(jsonFileData.read())
