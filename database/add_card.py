import sqlite3
import pandas as pd

def add_cards_from_csv(csv_path: str):
    # Load and sanitize CSV
    df = pd.read_csv(csv_path)
    df.columns = [col.strip() for col in df.columns]  # clean column names

    required_columns = {"name", "intelligence", "power", "hp", "defense", "mobility", "stealth", "g_max"}
    if not required_columns.issubset(set(df.columns)):
        raise ValueError(f"CSV is missing required columns. Found: {df.columns.tolist()}")

    conn = sqlite3.connect("game_of_life.db")
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
        INSERT OR REPLACE INTO cards (
            id, name, intelligence, power, hp, defense, mobility, stealth, g_max
        )
        VALUES (
            COALESCE((SELECT id FROM cards WHERE name = ? COLLATE NOCASE), NULL),
            ?, ?, ?, ?, ?, ?, ?, ?
        )
        """, (
            row["name"],  # for SELECT
            row["name"], row["intelligence"], row["power"], row["hp"],
            row["defense"], row["mobility"], row["stealth"], row["g_max"]
        ))

    conn.commit()
    conn.close()
    print(f"Inserted/Updated {len(df)} cards from {csv_path}")

if __name__ == "__main__":
    add_cards_from_csv("cards.csv")  