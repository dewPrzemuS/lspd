import os

from flask import Flask

from routes.error import error_bp
from routes.home import home_bp

app = Flask(__name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Leave it like this!

app.register_blueprint(home_bp)

if __name__ == "__main__":
    # sys.setdefaultencoding('utf8mb4_polish_ci')
    app.config['JSON_AS_ASCII'] = False
    app.config['RESTFUL_JSON'] = {
        'ensure_ascii': False
    }
    app.run(debug=False)
