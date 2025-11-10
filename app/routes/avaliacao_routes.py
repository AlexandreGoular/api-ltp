
from app.extensions import bcrypt
from flask import Blueprint, request, jsonify
from app.dao.avaliacao_dao import AvaliacaoDAO
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_bcrypt import Bcrypt 

login = {
    "user": "",
    "senha": ""
}

avaliacao_bp = Blueprint("avaliacao", __name__)

@avaliacao_bp.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    login["user"] = data['nome']
    login["senha"] = bcrypt.generate_password_hash( data['senha']).decode("utf-8")
    return jsonify({"message": "Login criado"})

@avaliacao_bp.route("/login", methods=["POST"])
def hello():
    data = request.get_json()
    isEqual = bcrypt.check_password_hash(login['senha'], data['senha'])
    if login['user'] == data['nome'] and isEqual:
        token = create_access_token(identity=login["user"])
        return jsonify({"message": "Bem vindo", "token": token})
    else:
        return jsonify({"message": "Erro ao efetuar login"})

@avaliacao_bp.route("/", methods=["GET"])
@jwt_required()
def list_avaliacoes():
    avaliacoes = AvaliacaoDAO.get_all_avaliacoes()
    return jsonify([{"id": u.id, "email": u.email, "avaliacao": u.avaliacao} for u in avaliacoes])

@avaliacao_bp.route("/", methods=["POST"])
def create_avaliacao():
    data = request.get_json()
    if not data or "email" not in data or "avaliacao" not in data:
        return jsonify({"error": "Campos 'email' e 'avaliacao' são obrigatorios"}), 400 
    AvaliacaoDAO.create(data["email"], data["avaliacao"])
    return jsonify({"message": "Avalicao criada"}), 201

@avaliacao_bp.route("/<int:avaliacao_id>", methods=["DELETE"])
def delete_avaliacao(avaliacao_id):
    AvaliacaoDAO.delete_avaliacao_by_id(avaliacao_id)
    return jsonify({"message": f"Avaliacao {avaliacao_id} deletada com sucesso"}), 200 

@avaliacao_bp.route("/<int:avaliacao_id>", methods=["PUT"])
def update_avaliacao(avaliacao_id):
    data = request.get_json()
    if not data or "avaliacao" not in data:
        return jsonify({"error": "Campo avaliacao obrigatorio"}), 400 
    AvaliacaoDAO.update_avaliacao_by_id(data["avaliacao"], avaliacao_id)
    return jsonify({"message": f"Avaliacao {avaliacao_id} atualizada com sucesso"}), 200

@avaliacao_bp.route("/<int:avaliacao_id>", methods=["GET"])
@jwt_required()
def get_avaliacao(avaliacao_id):
    avaliacao = AvaliacaoDAO.get_avaliacao_by_id(avaliacao_id)
    if avaliacao:
        return jsonify({
            "id": avaliacao[0],
            "email": avaliacao[1],
            "avaliacao": avaliacao[2]
        })


