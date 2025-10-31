from flask import Flask
from app.database.db import init_db
from app.routes.avaliacao_routes import avaliacao_bp
from app.extensions import bcrypt, jwt
import os

app = Flask(__name__)
init_db()

app.config["JWT_SECRET_KEY"] = "super_secret_key"

bcrypt.init_app(app)
jwt.init_app(app)

app.register_blueprint(avaliacao_bp, url_prefix="/avaliacoes")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = os.environ.get('PORT', 3000))

