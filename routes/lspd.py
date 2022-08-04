from flask import Blueprint, render_template, request

from functions.other import dataLspd, getalnum

lspd_bp = Blueprint('LSPD', __name__)


@lspd_bp.route("/lspd", methods=["GET"])
def lspdGet():
    global amount0
    amount0 = 0
    global amount1
    amount1 = 0
    global amount2
    amount2 = 0
    global howMany
    howMany = 0

    return render_template("lspd.html", data=dataLspd, getalnum=getalnum, len=len, amount0=amount0, amount1=amount1,
                           amount2=amount2, display=False)


@lspd_bp.route("/lspd", methods=["POST"])
def lspdPost():
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
    penaltyType = ""
    global division
    global display
    global selected
    selected = []
    display = True
    global explanations
    explanations = ""
    if request.form.get("range") == "0":
        penaltyType = "Minimalny"
    if request.form.get("range") == "1":
        penaltyType = "Niski"
        division = 3
    if request.form.get("range") == "2":
        penaltyType = "Zwykły"
        division = 2
    if request.form.get("range") == "3":
        penaltyType = "Maksymalny"
        division = 1
    for d in dataLspd:
        value = request.form.get(f"option{getalnum(d)}")
        if value is None:
            continue
        if dataLspd[value]["explanation"] != "null":
            explanations += dataLspd[value]["explanation"] + ", "
        selected.append(d)
        pp += dataLspd[value]["pp"]
        if request.form.get("range") == "0":
            fine += dataLspd[value]["minfine"]
            jail += dataLspd[value]["minjail"]
        else:
            if dataLspd[value]["fine"] / division < dataLspd[value]["minfine"]:
                fine += dataLspd[value]["minfine"]
            else:
                fine += (dataLspd[value]["fine"] / division)
            if dataLspd[value]["minjail"] / division < dataLspd[value]["minjail"]:
                jail += dataLspd[value]["minjail"]
            else:
                jail += (dataLspd[value]["jail"] / division)
            if dataLspd[value]["jailorfine"]:
                if request.form.get("jailorfine") != "on":
                    jail -= (dataLspd[value]["jail"] / division)
                else:
                    fine -= (dataLspd[value]["fine"] / division)
    fine = round(fine)
    pp = round(pp)
    jail = round(jail)
    if jail > 250:
        jail = 250
    if fine > 5000:
        fine = 5000

    explanations = explanations[:-2] + "."

    return render_template("lspd.html", data=dataLspd, getalnum=getalnum, len=len, fine=fine, pp=pp, jail=jail,
                           display=display, round=round, amount0=amount0, amount1=amount1,
                           amount2=amount2, selected=selected, penaltyType=penaltyType, explanations=explanations)
