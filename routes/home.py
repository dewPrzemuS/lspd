import os

from flask import Blueprint, redirect, render_template, request
import json

jsonFile = open(f"{os.path.dirname(os.path.realpath(__file__))}/data.json")

data = json.loads(jsonFile.read())

home_bp = Blueprint('Home', __name__)

global version
version = "1.1"

def getalnum(string):
    alphanumeric = [character for character in string if character.isalnum()]
    return "".join(alphanumeric)


@home_bp.route("/", methods=["GET"])
def homeget():
    return render_template("index.html", data=data, getalnum=getalnum, len=len)


@home_bp.route("/", methods=["POST"])
def homepost():
    fine = 0
    pp = 0
    jail = 0
    global division
    global display
    display = True
    if request.form.get("range") == "0":
        division = 3
    if request.form.get("range") == "1":
        division = 2
    if request.form.get("range") == "2":
        division = 1
    for d in data:
        value = request.form.get(f"option{getalnum(d)}")
        if value is None:
            continue
        fine += (data[value]["fine"] / division)
        pp += (data[value]["pp"] / division)
        jail += (data[value]["jail"] / division)
        fine = round(fine)
        pp = round(pp)
        jail = round(jail)
    if fine == 0 and pp == 0 and jail == 0:
        display = False
    return render_template("index.html", data=data, getalnum=getalnum, len=len, fine=fine, pp=pp, jail=jail, display=display, round=round, version=version)
