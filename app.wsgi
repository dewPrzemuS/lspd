import sys

sys.path.insert(0, "/var/www/taryfikatory-prl")

activate_this = "/var/www/taryfikatory-prl/venv/bin/activate_this.py"

with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from app import app as application