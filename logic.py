import sqlite3
from database import DB_PATH
from datetime import datetime

def calcular_racha_disciplina():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT ejecucion_correcta FROM daily_log ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    racha = 0
    for row in rows:
        if row[0] == 1:
            racha += 1
        else:
            break
    return racha

def promedio_checklist():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT AVG(checklist_percent) FROM daily_log")
    avg = c.fetchone()[0]
    conn.close()
    return avg if avg else 0
