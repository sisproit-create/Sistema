import streamlit as st

from state_init import init_session_state
init_session_state()

from database import init_db
from logic import calcular_racha_disciplina
from config import CAPITAL_INICIAL

init_db()

st.set_page_config(page_title="Sistema de Trading", layout="wide")

if "permiso_operar" not in st.session_state:
    st.session_state.permiso_operar = False

st.title("🧠 Sistema de Trading para Libertad Financiera")

st.markdown("### 🔒 El proceso manda. El dinero obedece.")

col1, col2, col3 = st.columns(3)

col1.metric("Capital Base", f"${CAPITAL_INICIAL}")
col2.metric("Racha Disciplina", calcular_racha_disciplina())
col3.metric("Permiso Hoy", "Sí" if st.session_state.permiso_operar else "No")
