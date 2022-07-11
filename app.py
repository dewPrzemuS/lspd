# from OpenSSL import SSL
from flask import Flask

from routes.index import index_bp
from routes.lspd import lspd_bp
# from routes.support import support_bp

app = Flask(__name__)

app.register_blueprint(lspd_bp)
# app.register_blueprint(support_bp)
app.register_blueprint(index_bp)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000, threaded=True)
