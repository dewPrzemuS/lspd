import os

from flask import Flask

from routes.home import home_bp

app = Flask(__name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Leave it like this!

app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=False)
