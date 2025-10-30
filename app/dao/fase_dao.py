from app.database.db import get_connection 
from app.models.fase import Missao 

class MissaoDAO:
    @staticmethod
    def create(titulo, descricao, dificuldade):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO missao (titulo, descricao, dificuldade) VALUES (?, ?, ?)", (titulo, descricao, dificuldade))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_missoes():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM missao")
        rows = cursor.fetchall()
        conn.close()
        return [Missao(row["id"], row["titulo"], row["descricao"], row["dificuldade"]) for row in rows]

    @staticmethod
    def delete_missao_by_id(missao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM missao WHERE id = ?", (missao_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update_missao_by_id(dificuldade, missao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE missao SET dificuldade = ? WHERE id = ?", (dificuldade, missao_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_missao_by_id(missao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM missao WHERE id = ?", (missao_id))
        row = cursor.fetchone()
        conn.close()
        return row 
