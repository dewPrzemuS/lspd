from datetime import datetime

from flask import Blueprint, render_template, request

from functions.other import data

home_bp = Blueprint('Home', __name__)


def getalnum(string):
    alphanumeric = [character for character in string if character.isalnum()]
    return "".join(alphanumeric)


@home_bp.route("/", methods=["GET"])
def homeget():
    today = datetime.now()
    global amount0
    amount0 = 0
    global amount1
    amount1 = 0
    global amount2
    amount2 = 0
    global howMany
    howMany = 0

    # results = getPenalties()
    # for result in results:
    #     value = result[0]
    #     if value == "0":
    #         amount0 += 1
    #     if value == "1":
    #         amount1 += 1
    #     if value == "2":
    #         amount2 += 1
    #     howMany += 1
    # if howMany > 0:
    #     amount0 = round((amount0 / howMany) * 100)
    #     amount1 = round((amount1 / howMany) * 100)
    #     amount2 = round((amount2 / howMany) * 100)

    return render_template("index.html", data=data, getalnum=getalnum, len=len, amount0=amount0, amount1=amount1,
                           amount2=amount2)


@home_bp.route("/", methods=["POST"])
def homepost():
    today = datetime.now()
    global amount0
    amount0 = 0
    global amount1
    amount1 = 0
    global amount2
    amount2 = 0
    global howMany
    howMany = 0
    fine = 0
    pp = 0
    jail = 0
    global division
    global display
    global selected
    selected = []
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
        selected.append(d)
        fine += (data[value]["fine"] / division)
        pp += data[value]["pp"]
        jail += (data[value]["jail"] / division)
        fine = round(fine)
        pp = round(pp)
        jail = round(jail)
        if fine < data[value]["minfine"]:
            fine = data[value]["minfine"]
        if jail < data[value]["minjail"]:
            jail = data[value]["minjail"]
    if fine == 0 and pp == 0 and jail == 0:
        display = False

    global stringSelected
    stringSelected = ""
    for select in selected:
        stringSelected += f"{select} "

    # results = getPenalties()
    # for result in results:
    #     value = result[0]
    #     if value == "0":
    #         amount0 += 1
    #     if value == "1":
    #         amount1 += 1
    #     if value == "2":
    #         amount2 += 1
    #     howMany += 1
    # if howMany > 0:
    #     amount0 = round((amount0 / howMany) * 100)
    #     amount1 = round((amount1 / howMany) * 100)
    #     amount2 = round((amount2 / howMany) * 100)

    return render_template("index.html", data=data, getalnum=getalnum, len=len, fine=fine, pp=pp, jail=jail,
                           display=display, round=round, amount0=amount0, amount1=amount1,
                           amount2=amount2, selected=selected)
