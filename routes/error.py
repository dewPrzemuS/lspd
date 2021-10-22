from flask import Blueprint, render_template

error_bp = Blueprint('Error', __name__)


@error_bp.app_errorhandler(400)
def error400(error):
    return render_template("errors/400.html")


@error_bp.app_errorhandler(401)
def error401(error):
    return render_template("errors/401.html")


@error_bp.app_errorhandler(403)
def error403(error):
    return render_template("errors/403.html")


@error_bp.app_errorhandler(404)
def error404(error):
    return render_template("errors/404.html")


@error_bp.app_errorhandler(423)
def error423(error):
    return render_template("errors/423.html")


@error_bp.app_errorhandler(500)
def error500(error):
    return render_template("errors/500.html")


@error_bp.app_errorhandler(503)
def error503(error):
    return render_template("errors/503.html")
