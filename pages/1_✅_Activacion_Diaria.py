import streamlit as st
from state_init import init_session_state

init_session_state()

st.title("✅ ACTIVACIÓN DIARIA")

# =========================
# INICIALIZACIÓN SEGURA
# =========================

if "permiso_operar" not in st.session_state:
    st.session_state.permiso_operar = False

# =========================
# 1️⃣ IDENTIDAD
# =========================

st.header("🧠 Identidad Operativa")

identidad_items = [
    "Soy una persona disciplinada y constante en el trading.",
    "Mi tarea diaria es ejecutar mi proceso sin improvisar",
    "Mi prioridad es control emocional, disciplina y respeto del proceso.",
    "Acepto pérdidas sin reaccionar."
]

identidad_checks = [st.checkbox(item, key=f"id_{i}") 
                    for i, item in enumerate(identidad_items)]

# =========================
# 2️⃣ DIRECCIÓN FINANCIERA
# =========================

st.header("🎯 Dirección Financiera")

direccion_items = [
    "Mi objetivo financiero es alcanzar un millón de dólares.",
    "Opero con un capital inicial de 800 USD, enfocado en duplicarlo con consistencia, no con prisa.",
    "Repito el proceso hasta que la constancia sea un hábito automático.",
    "Cuando el hábito está consolidado, incremento el capital y repito exactamente el mismo proceso.",
    "El dinero es consecuencia natural de ejecutar correctamente el sistema."
]

direccion_checks = [st.checkbox(item, key=f"dir_{i}") 
                    for i, item in enumerate(direccion_items)]

# =========================
# 3️⃣ MANTRA OPERATIVO DIARIO
# =========================

st.header("☀️ Mantra Operativo Diario")
st.caption("Leer en voz alta antes de abrir el mercado")

mantra_items = [
    "Hoy solo tengo una tarea: ejecutar mi proceso con disciplina.",
    "No persigo dinero, persigo consistencia.",
    "Mi capital crece como resultado de hacer bien el proceso, una y otra vez.",
    "Mantengo control emocional, sigo mis reglas y respeto mis invalidaciones.",
    "La constancia es mi ventaja.",
    "La constancia me lleva al millón."
]

mantra_checks = [st.checkbox(item, key=f"man_{i}") 
                 for i, item in enumerate(mantra_items)]

# =========================
# CÁLCULO TOTAL
# =========================

todos_checks = identidad_checks + direccion_checks + mantra_checks

total = len(todos_checks)
activos = sum(todos_checks)
percent = int((activos / total) * 100)

st.progress(percent / 100)
st.write(f"Cumplimiento total: {percent}%")

# =========================
# PERMISO FINAL
# =========================

if percent == 100:
    st.session_state.permiso_operar = True
    st.success("🟢 Permiso concedido para operar.")
else:
    st.session_state.permiso_operar = False
    st.error("🔴 No autorizado para operar. Debes completar todo.")
