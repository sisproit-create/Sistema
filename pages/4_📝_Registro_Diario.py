import streamlit as st

from state_init import init_session_state
init_session_state()

import sqlite3
from database import DB_PATH
from datetime import datetime

st.title("📝 CIERRE Y REGISTRO DIARIO")

st.subheader("Evaluación no monetaria")

p1 = st.checkbox("Seguí el proceso")
p2 = st.checkbox("Respeté reglas")
p3 = st.checkbox("Controlé emociones")

emocional = st.selectbox("Estado emocional final",
                         ["Estable", "Ansioso", "Disperso"])

checklist_percent = st.session_state.get("checklist_percent",0)

if st.button("Guardar Día"):
    ejecucion = 1 if p1 and p2 and p3 else 0

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO daily_log 
        (fecha, checklist_percent, ejecucion_correcta, emocional_post, operaciones_totales)
        VALUES (?,?,?,?,?)
    """, (datetime.now().date(), checklist_percent,
          ejecucion,
          emocional, 0))
    conn.commit()
    conn.close()

    st.success("Día registrado correctamente.")
