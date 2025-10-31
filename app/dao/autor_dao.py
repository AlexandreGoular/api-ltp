from app.database.db import get_connection
from app.models.autor import Autor

class AutorDAO:
    @staticmethod
    def create(nome, descricao):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO autor (nome, descricao) VALUES (?, ?)", (nome, descricao))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_autors():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM autor")
        rows = cursor.fetchall()
        conn.close()
        return [Autor(row["id"], row["nome"], row["descricao"]) for row in rows]

    @staticmethod
    def delete_autor_by_id(autor_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM autor WHERE id = ?", (autor_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_autor_by_id(autor, autor_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE autor SET autor = ? WHERE id = ?", (autor, autor_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_autor_by_id(autor_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM autor WHERE id = ?", (autor_id, ))
        row = cursor.fetchone()
        conn.close()
        return row 
