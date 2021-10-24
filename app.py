import os

# from OpenSSL import SSL
from flask import Flask

from routes.home import home_bp

app = Flask(__name__)

# context = SSL.Context(SSL.SSLv23_METHOD)
# cer = os.path.join(os.path.dirname(__file__), 'resources/udara.com.crt')
# key = os.path.join(os.path.dirname(__file__), 'resources/udara.com.key')


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Leave it like this!

app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
