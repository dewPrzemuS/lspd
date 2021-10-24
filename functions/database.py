import json
import os

import mysql.connector

jsonFileMySQL = open(f"{os.path.dirname(os.path.realpath(__file__))}/special/mysql.json")
sql = json.loads(jsonFileMySQL.read())

db = mysql.connector.connect(
    host=sql["host"],
    user="lspd",
    password=sql["password"],
    database="lspd"
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
