from flask import Blueprint, request, jsonify
from app.dao.player_dao import PlayerDAO

player_bp = Blueprint("player", __name__)

@player_bp.route("/", methods=["POST"])
def create_player():
    data = request.get_json()
    if not data or "nome" not in data or "classe" not in data or "vida" not in data:
        return jsonify({"error": "Campos 'nome', 'classe' e 'vida' são obrigatórios"}), 400
    
    PlayerDAO.create(data["nome"], data["classe"], data["vida"])
    return jsonify({"message": "Player criado com sucesso"}), 201


@player_bp.route("/<int:player_id>", methods=["DELETE"])
def delete_player(player_id):
    PlayerDAO.delete_player(player_id)
    return jsonify({"message": f"Player {player_id} deletado com sucesso"}), 200


@player_bp.route("/<int:player_id>", methods=["PUT"])
def update_player(player_id):
    data = request.get_json()
    if not data or "vida" not in data:
        return jsonify({"error": "Campo 'vida' é obrigatório"}), 400
    
    PlayerDAO.update_player(data["vida"], player_id)
    return jsonify({"message": f"Player {player_id} atualizado com sucesso"}), 200


@player_bp.route("/<int:player_id>", methods=["GET"])
def get_player(player_id):
    player = PlayerDAO.get_player(player_id)
    if player:
        return jsonify({
            "id": player[0],
            "nome": player[1],
            "classe": player[2],
            "vida": player[3]
        }), 200
    return jsonify({"error": "Player não encontrado"}), 404

