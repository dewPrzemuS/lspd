from flask import request


def getIP():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return ['HTTP_X_FORWARDED_FOR']
