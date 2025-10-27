from app.database.db import get_connection
from app.models.avaliacao import Avaliacao

class AvaliacaoDAO:
    @staticmethod
    def create(email, avaliacao):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO avaliacao (email, avaliacao) VALUES (?, ?)", (email, avaliacao))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_avaliacoes():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM avaliacao")
        rows = cursor.fetchall()
        conn.close()
        return [Avaliacao(row["id"], row["email"], row["avaliacao"]) for row in rows]

    @staticmethod
    def delete_avaliacao_by_id(avaliacao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM avaliacao WHERE id = ?", (avaliacao_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_avaliacao_by_id(avaliacao, avaliacao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE avaliacao SET avaliacao = ? WHERE id = ?", (avaliacao, avaliacao_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_avaliacao_by_id(avaliacao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM avaliacao WHERE id = ?", (avaliacao_id, ))
        row = cursor.fetchone()
        conn.close()
        return row 
