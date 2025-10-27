import sqlite3

DB_NAME = "dungeons_souls.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn 

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS avaliacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        avaliacao TEXT NOT NULL
    )
    """
    )
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        classe TEXT NOT NULL,
        vida INTEGER NOT NULL
    )
    """
    )
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS missao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL, 
        descricao TEXT NOT NULL,
        dificuldade TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(id)
    )
    """
    )

    conn.commit()
    conn.close()
