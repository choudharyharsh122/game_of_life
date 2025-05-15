import sqlite3

def init_db():
    # Connect to (or create) the database
    conn = sqlite3.connect("game_of_life.db")
    cursor = conn.cursor()

    # Create the 'cards' table
    cursor.execute("""
CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE COLLATE NOCASE,
    intelligence INTEGER NOT NULL,
    power INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    mobility INTEGER NOT NULL,
    stealth INTEGER NOT NULL,
    g_max INTEGER NOT NULL
)
""")

    # Sample animal cards
    sample_cards = [
        ("Lion",   60, 85, 78, 75, 82, 74, 6),
        ("Rat",    66, 10, 15, 10, 68, 72, 5),
        ("Spider", 15, 48, 8, 15, 58, 55, 1)
    ]

    # Insert sample cards
    cursor.executemany("""
    INSERT INTO cards (
        name, intelligence, power, hp, defense, mobility, stealth, g_max
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_cards)
 
    conn.commit()
    conn.close()
    print("Database initialized with sample cards.")

if __name__ == "__main__":
    init_db()
