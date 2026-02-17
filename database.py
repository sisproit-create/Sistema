import sqlite3
import os

DB_PATH = "data/trading.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS daily_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        checklist_percent INTEGER,
        ejecucion_correcta INTEGER,
        emocional_post TEXT,
        operaciones_totales INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        setup TEXT,
        riesgo REAL,
        hora TEXT
    )
    """)

    conn.commit()
    conn.close()
