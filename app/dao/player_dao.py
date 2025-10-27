from app.database.db import get_connection 
from app.models.player import Player

class PlayerDAO:
    @staticmethod
    def create(nome, classe, vida):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO player (nome, classe, vida) VALUES (?, ?, ?)", (nome, classe, vida))
        conn.commit()
        conn.close()

    @staticmethod
    def get_player(player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player WHERE id = ?", (player_id, ))
        row = cursor.fetchone()
        conn.close()
        return row 

    @staticmethod 
    def update_player(vida, player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE player SET vida = ? WHERE id = ?", (vida, player_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_player(player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM player WHERE id = ?", (player_id, ))
        conn.commit()
        conn.close()
