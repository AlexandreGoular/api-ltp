from flask import Blueprint, request, jsonify 
from app.dao.autor_dao import AutorDAO

autor_bp = Blueprint("autor", __name__)

@autor_bp.route("/", methods=["GET"])
def list_autors():
    autores = AutorDAO.get_all_autors()
    return jsonify([{"id": u.id, "nome": u.nome, "descricao": u.descricao} for u in missoes])

@autor_bp.route("/", methods=["POST"])
def create_autor():
    data = request.get_json()
    if not data or "nome" not in data or "descricao":
        return jsonify({"error": "Campos 'nome', 'descricao' são obrigatorios"}), 400 
    AutorDAO.create(data["nome"], data["descricao"])
    return jsonify({"message": "Autor criado"}), 201 

@autor_bp.route("/<int:autor_id>", methods=["DELETE"])
def delete_autor(autor_id):
    AutorDAO.delete_autor_by_id(autor_id)
    return jsonify({"message": f"Autor {autor_id} deletado com sucesso"}), 200 

@autor_bp.route("/<int:autor_id>", methods=["PUT"])
def update_autor(autor_id):
    data = request.get_json()
    if not data or "descricao" not in data:
        return jsonify({"error": "Campo descricao obrigatorio"}), 400 
    AutorDAO.update_autor_by_id(data["descricao"], autor_id)
    return jsonify({"message": f"Autor {autor_id} atualizado com sucesso"}), 200  

@autor_bp.route("/<int:autor_id>", methods=["GET"])
def get_autor(autor_id):
    autor = AutorDAO.get_autor_by_id(autor_id)
    if autor:
        return jsonify({
            "id": autor[0],
            "nome": autor[1],
            "descricao": autor[2]
        })
