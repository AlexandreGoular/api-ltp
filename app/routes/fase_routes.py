from flask import Blueprint, request, jsonify 
from app.dao.fase_dao import MissaoDAO

fase_bp = Blueprint("fase", __name__)

@fase_bp.route("/", methods=["GET"])
def list_missoes():
    missoes = MissaoDAO.get_all_missoes()
    return jsonify([{"id": u.id, "titulo": u.titulo, "descricao": u.descricao, "dificuldade": u.dificuldade} for u in missoes])

@fase_bp.route("/", methods=["POST"])
def create_missao():
    data = request.get_json()
    if not data or "titulo" not in data or "descricao" not in data or "dificuldade" not in data:
        return jsonify({"error": "Campos 'titulo', 'descricao' e 'dificuldade' são obrigatorios"}), 400 
    MissaoDAO.create(data["titulo"], data["descricao"], data["dificuldade"])
    return jsonify({"message": "Missao criada"}), 201 

@fase_bp.route("/<int:missao_id>", methods=["DELETE"])
def delete_missao(missao_id):
    MissaoDAO.delete_missao_by_id(missao_id)
    return jsonify({"message": f"Missao {missao_id} deletada com sucesso"}), 200 

@fase_bp.route("/<int:missao_id>", methods=["PUT"])
def update_missao(missao_id):
    data = request.get_json()
    if not data or "dificuldade" not in data:
        return jsonify({"error": "Campo dificuldade obrigatorio"}), 400 
    MissaoDAO.update_missao_by_id(data["dificuldade"], missao_id)
    return jsonify({"message"}: f"Missao {missao_id} atualizada com sucesso"}), 200  

@fase_bp.route("/<int:missao_id>", methods=["GET"])
def get_missao(missao_id):
    missao = MissaoDAO.get_missao_by_id(missao_id)
    if missao:
        return jsonify({
            "id": missao[0],
            "titulo": missao[1],
            "descricao": missao[2],
            "dificuldade": missao[3]
        })
