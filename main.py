from flask import Flask 
from app.database.db import init_db
from app.routes.avaliacao_routes import avaliacao_bp 


app = Flask(__name__)
init_db()


app.register_blueprint(avaliacao_bp, url_prefix="/avaliacoes")

if __name__ == "__main__":
    app.run(debug=True)
