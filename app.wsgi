import sys

sys.path.insert(0, "/var/www/lspd")

activate_this = "/var/www/lspd/env/bin/activate"

with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from app import app as application