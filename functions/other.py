from flask import request


def getIP():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return str(request.environ['REMOTE_ADDR'])
    else:
        return str(request.environ['HTTP_X_FORWARDED_FOR'])
