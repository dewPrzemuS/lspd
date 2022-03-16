import os

# from OpenSSL import SSL
from flask import Flask

from routes.error import error_bp
from routes.home import home_bp

app = Flask(__name__)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"  # !! Only in development environment.

app.register_blueprint(home_bp)
app.register_blueprint(error_bp)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
