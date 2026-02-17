import streamlit as st

from state_init import init_session_state
init_session_state()

from logic import promedio_checklist, calcular_racha_disciplina

st.title("📈 CAPA DE ESCALADO")

promedio = promedio_checklist()
racha = calcular_racha_disciplina()

st.metric("Promedio Checklist", f"{round(promedio,1)}%")
st.metric("Racha Disciplina", racha)

st.write("Escalado progresivo:")
st.write("800 → 1,600 → 3,200 → 5,000 → 10,000 → 25,000 → 100,000")

if promedio >= 90 and racha >= 20:
    st.success("Condiciones mínimas cumplidas para escalar.")
else:
    st.error("Aún no cumple condiciones de disciplina.")
