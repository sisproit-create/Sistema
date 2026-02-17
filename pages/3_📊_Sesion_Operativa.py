import streamlit as st
from datetime import datetime, time
import pytz
from config import CAPITAL_INICIAL, RIESGO_PORCENTAJE, SETUPS_PERMITIDOS

st.title("📊 EJECUCIÓN CONTROLADA")

# ==============================
# INICIALIZAR CAPITAL DINÁMICO
# ==============================

if "capital_actual" not in st.session_state:
    st.session_state.capital_actual = CAPITAL_INICIAL

capital_actual = st.session_state.capital_actual
riesgo_diario_max = capital_actual * RIESGO_PORCENTAJE

# ==============================
# VALIDACIÓN DE HORARIO NY
# ==============================

ny = pytz.timezone("America/New_York")
hora_actual = datetime.now(ny).time()

inicio = time(9, 30)
fin = time(11, 0)

if not (inicio <= hora_actual <= fin):
    st.error("Fuera del horario permitido (9:30 AM - 11:00 AM NY).")
    st.stop()

# ==============================
# PANEL DE CONTROL
# ==============================

st.markdown("### 📊 Estado de Cuenta")
st.write(f"Capital actual: **${capital_actual:.2f}**")
st.write(f"Riesgo diario permitido (2%): **${riesgo_diario_max:.2f}**")

# ==============================
# FORMULARIO OPERACIÓN
# ==============================

st.subheader("📌 Datos de la Operación")

setup = st.selectbox("Tipo de Setup", SETUPS_PERMITIDOS)

riesgo = st.number_input(
    "Riesgo de la operación ($)",
    min_value=0.0,
    step=1.0
)

resultado = st.number_input(
    "Resultado de la operación ($)  (positivo o negativo)",
    step=1.0
)

comentario = st.text_area("Notas de la operación")

# ==============================
# EJECUTAR
# ==============================

if st.button("🚀 Ejecutar Operación"):

    # Validar riesgo permitido
    if riesgo > riesgo_diario_max:
        st.error(f"Riesgo excede el máximo diario permitido (${riesgo_diario_max:.2f}).")
        st.stop()

    # Actualizar capital según resultado
    st.session_state.capital_actual += resultado

    st.success("Operación registrada correctamente.")

    st.write("Nuevo capital:", f"${st.session_state.capital_actual:.2f}")
