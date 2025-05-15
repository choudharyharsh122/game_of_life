import sqlite3

DB_PATH = "game_of_life.db"

def get_card_data_by_name(name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_cards():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards")
    result = cursor.fetchall()
    conn.close()
    return result
