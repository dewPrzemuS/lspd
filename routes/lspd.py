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


# create class/object of Explanation that contains the explanation and type of explanation

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

    global fineExplanations
    fineExplanations = ""

    global jailExplanations
    jailExplanations = ""
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

        selected.append(d)
        pp += dataLspd[value]["pp"]
        if request.form.get("range") == "0":
            if dataLspd[value]["jailorfine"]:
                if request.form.get("jailorfine") == "on":
                    jail += dataLspd[value]["minjail"]
                    if jail < 1 and dataLspd[value]["jail"] > 0:
                        jail += 1
                else:
                    fine += dataLspd[value]["minfine"]
                    if fine < 1 and dataLspd[value]["fine"] > 0:
                        fine += 1
            else:
                jail += dataLspd[value]["minjail"]
                if jail < 1 and dataLspd[value]["jail"] > 0:
                    jail += 1
                fine += dataLspd[value]["minfine"]
                if fine < 1 and dataLspd[value]["fine"] > 0:
                    fine += 1
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

        # if explanation is not empty
        if dataLspd[value]["explanation"] != "":
            # if data is jailorfine
            if dataLspd[value]["jailorfine"]:
                # if jailorfine is on
                if request.form.get("jailorfine") == "on":
                    # if jail is greater than 0
                    if dataLspd[value]["jail"] > 0:
                        # add explanation to list
                        jailExplanations += dataLspd[value]["explanation"] + ", "
                else:
                    # if fine is greater than 0
                    if dataLspd[value]["fine"] > 0:
                        # add explanation to list
                        fineExplanations += dataLspd[value]["explanation"] + ", "
            else:
                if dataLspd[value]["jail"] > 0:
                    # add explanation to list
                    jailExplanations += dataLspd[value]["explanation"] + ", "
                if dataLspd[value]["fine"] > 0 or dataLspd[value]["pp"] > 0:
                    # add explanation to list
                    fineExplanations += dataLspd[value]["explanation"] + ", "
    fine = round(fine)
    pp = round(pp)
    jail = round(jail)

    if jail > 250:
        jail = 250
    if fine > 5000:
        fine = 5000

    jailExplanations = jailExplanations[:-2] + "."
    fineExplanations = fineExplanations[:-2] + "."

    return render_template("lspd.html", data=dataLspd, getalnum=getalnum, len=len, fine=fine, pp=pp, jail=jail,
                           display=display, round=round, amount0=amount0, amount1=amount1,
                           amount2=amount2, selected=selected, penaltyType=penaltyType, fineExplanations=fineExplanations, jailExplanations=jailExplanations)
