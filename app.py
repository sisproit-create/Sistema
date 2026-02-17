import streamlit as st
from database import init_db
from logic import calcular_racha_disciplina, promedio_checklist
from config import CAPITAL_INICIAL

init_db()

st.set_page_config(page_title="Sistema Operativo de Trading", layout="wide")

# ---- SESSION STATE ----
if "permiso_operar" not in st.session_state:
    st.session_state.permiso_operar = False

if "mantra_activado" not in st.session_state:
    st.session_state.mantra_activado = False

if "checklist_percent" not in st.session_state:
    st.session_state.checklist_percent = 0

st.title("🧠 SISTEMA DE TRADING PARA LIBERTAD FINANCIERA")
st.markdown("### 🔒 El proceso manda. El dinero obedece.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Capital Base", f"${CAPITAL_INICIAL}")
col2.metric("Racha Disciplina", calcular_racha_disciplina())
col3.metric("Promedio Checklist", f"{round(promedio_checklist(),1)}%")
col4.metric("Permiso Hoy", "Sí" if st.session_state.permiso_operar else "No")
