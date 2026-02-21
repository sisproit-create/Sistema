import streamlit as st
from state_init import init_session_state

init_session_state()

st.title("📊 Sistema de Trading para Libertad Financiera")

st.markdown("---")

# =========================================================
# ☀️ MANTRA OPERATIVO DIARIO
# =========================================================

st.header("☀️ MANTRA OPERATIVO DIARIO")
st.caption("Leer en voz alta antes de abrir el mercado")

st.markdown("""
☐ Hoy solo tengo una tarea: ejecutar mi proceso con disciplina.  
☐ No persigo dinero, persigo consistencia.  
☐ Mi capital crece como resultado de hacer bien el proceso, una y otra vez.  
☐ Mantengo control emocional, sigo mis reglas y respeto mis invalidaciones.  
☐ La constancia es mi ventaja.  
☐ La constancia me lleva al millón.
""")

st.markdown("---")

# =========================================================
# 🧠 MANUAL OPERATIVO
# =========================================================

st.header("🧠 MANUAL OPERATIVO")
st.subheader("SISTEMA DE TRADING PARA LIBERTAD FINANCIERA")

st.markdown("""
## 🔒 Principio Rector
**El proceso manda. El dinero obedece.**
""")

# ---------------------------------------------------------
# 1️⃣ OBJETIVO
# ---------------------------------------------------------

st.markdown("""
## 1️⃣ OBJETIVO DEL SISTEMA

Construir disciplina, constancia y control emocional mediante la ejecución repetida de un proceso simple de trading, con el fin de escalar capital de forma progresiva hasta alcanzar libertad financiera.

Este sistema no existe para ganar hoy.  
Existe para sostener resultados en el tiempo.
""")

# ---------------------------------------------------------
# 2️⃣ IDENTIDAD OPERATIVA
# ---------------------------------------------------------

st.markdown("""
## 2️⃣ IDENTIDAD OPERATIVA (ANTES DE OPERAR)

Antes de abrir el mercado, confirmo:

• Soy una persona disciplinada y constante.  
• Mi tarea es ejecutar el proceso, no perseguir dinero.  
• Opero solo si estoy emocionalmente estable.  
• Acepto pérdidas sin reaccionar.  

📌 Si esta identidad no está activa, no opero.
""")

# ---------------------------------------------------------
# 3️⃣ ACTIVACIÓN DIARIA
# ---------------------------------------------------------

st.markdown("""
## 3️⃣ ACTIVACIÓN DIARIA (FILTRO DE PERMISO)

Solo opero si todas son afirmativas:

☐ Leí el mantra operativo.  
☐ Revisé el checklist diario.  
☐ El mercado cumple mis condiciones.  
☐ Estoy dispuesto a cerrar sesión aunque pierda.  

❌ Una sola negativa = no operar.

Este filtro protege el capital y protege la mente.
""")

# ---------------------------------------------------------
# 4️⃣ EJECUCIÓN CONTROLADA
# ---------------------------------------------------------

st.markdown("""
## 4️⃣ EJECUCIÓN CONTROLADA

Durante la sesión:

• Opero únicamente Setups A / B / C.  
• Respeto el riesgo diario máximo definido.  
• Opero dentro del horario establecido (cierro aunque el mercado siga).  
• No improviso.  
• No intento “recuperar”.  

📌 Si una operación no encaja claramente en el sistema, no existe.
""")

# ---------------------------------------------------------
# 5️⃣ CIERRE DE SESIÓN
# ---------------------------------------------------------

st.markdown("""
## 5️⃣ CIERRE DE SESIÓN (OBLIGATORIO)

Al finalizar:

• Cierro la plataforma.  
• No reviso el mercado después.  
• No agrego operaciones tardías.  

### Evaluación diaria (no monetaria)

☐ Seguí el proceso.  
☐ Respeté mis reglas.  
☐ Controlé mis emociones.  

📌 Un día bien ejecutado es un día ganado, incluso si hubo pérdida.
""")

# ---------------------------------------------------------
# 6️⃣ BUCLE DE CONSISTENCIA
# ---------------------------------------------------------

st.markdown("""
## 6️⃣ BUCLE DE CONSISTENCIA

El sistema se ejecuta igual todos los días.

Repetición → Hábito → Confianza → Consistencia  

No busco perfección.  
Busco repetición correcta.
""")

# ---------------------------------------------------------
# 7️⃣ ESCALADO
# ---------------------------------------------------------

st.markdown("""
## 7️⃣ ESCALADO DE CAPITAL (REGLA NO NEGOCIABLE)

El capital solo aumenta si se cumplen todas las condiciones:

• X meses consecutivos siguiendo el sistema.  
• Drawdown controlado.  
• Checklist cumplido ≥ 90%.  

📌 No subo capital por ganar dinero.  
Subo capital por buen comportamiento.  

El comportamiento precede al crecimiento.
""")

# ---------------------------------------------------------
# 8️⃣ RESULTADO ESPERADO
# ---------------------------------------------------------

st.markdown("""
## 8️⃣ RESULTADO ESPERADO (NO OPERATIVO)

Si el sistema se ejecuta correctamente:

• Ingresos más estables.  
• Menos horas frente al mercado.  
• Mayor claridad mental.  
• Transferencia progresiva a activos pasivos.  
• Más tiempo libre.  

La libertad es consecuencia del proceso sostenido.
""")

# ---------------------------------------------------------
# 🔒 REGLA FINAL
# ---------------------------------------------------------

st.markdown("""
## 🔒 REGLA FINAL DEL SISTEMA

Cada día solo importa una pregunta:

**¿Ejecuté el sistema correctamente?**

Si la respuesta es sí, el sistema está funcionando.  
El dinero llegará como efecto secundario.
""")

st.markdown("---")
st.header("🧠 MARCO TÉCNICO DE EJECUCIÓN")

# =========================================================
# 1️⃣ CONTEXTO
# =========================================================

st.subheader("1️⃣ CONTEXTO (Antes de ver el gráfico)")

st.markdown("""
### 🔎 ¿Qué significa realmente?

Antes de mirar velas pequeñas, necesitas entender el ambiente.
""")

with st.expander("Macro / Noticias"):

    st.markdown("""
Ejemplos de noticias que mueven mercado:

• Datos de inflación (CPI)  
• Decisiones de la Fed  
• Nóminas (NFP)  
• Resultados de empresas grandes (Amazon, Apple)

### Cómo interpretarlo:

**Hay noticia fuerte hoy**
• Más volatilidad  
• Movimientos violentos  
• Falsas rupturas frecuentes  
• Dirección menos confiable al inicio  

**No hay noticia**
• Mejor respeto de niveles técnicos  
• Estructura más limpia  

### Regla clave:
No operas la noticia.  
Operas cómo el precio REACCIONA a ella.

Ejemplo:
Sale CPI fuerte → mercado cae.  
Pero si recupera VWAP con volumen → eso es lo que operas.
""")

# =========================================================
# 2️⃣ ESTRUCTURA
# =========================================================

st.subheader("2️⃣ ESTRUCTURA (Dónde estamos)")

with st.expander("🔹 Tendencia"):
    st.markdown("""
Características:
• HH (Higher High)  
• HL (Higher Low)  
• Precio sobre VWAP  
• Medias inclinadas  

👉 Interpretación:
El mercado acepta precios más altos.

👉 Aplicación:
No vendes.  
Buscas retrocesos para entrar a favor.
""")

with st.expander("🔹 Rango"):
    st.markdown("""
Características:
• Máximos y mínimos respetados  
• VWAP plana  
• Mechas arriba y abajo  

👉 Interpretación:
Institucionales acumulando o distribuyendo.

👉 Aplicación:
Vendes en techo  
Compras en piso  
Tomas ganancias rápido
""")

with st.expander("🔹 Transición"):
    st.markdown("""
Características:
• Ruptura que falla  
• Velas grandes con rechazo  
• Volumen inconsistente  

👉 Interpretación:
El mercado está decidiendo dirección.

👉 Aplicación:
Esperar confirmación.
Aquí se pierde dinero si te anticipas.
""")

# =========================================================
# 3️⃣ NIVELES CLAVE
# =========================================================

st.subheader("3️⃣ NIVELES CLAVE")

st.markdown("""
Esto se marca ANTES de que abra el mercado:

• PDH (Previous Day High)  
• PDL (Previous Day Low)  
• High / Low de premarket  
• VWAP  
• Números redondos (.00 / .50)

¿Por qué?

Porque instituciones miran lo mismo.
Son zonas donde:

• Se activa liquidez  
• Se ejecutan órdenes grandes  
• Se producen falsas rupturas  

Sin niveles, operas en el vacío.
""")

# =========================================================
# 4️⃣ SETUP
# =========================================================

st.subheader("4️⃣ SETUP (Cuándo es operable)")

st.markdown("""
Un trade válido necesita 3 confirmaciones:

1️⃣ Nivel  
Sin nivel = azar.

2️⃣ Vela  
• Rechazo (mecha larga)  
• Engulfing  
• Break & Retest  

3️⃣ Volumen  
• Aumenta en ruptura → confirmación  
• Disminuye en retroceso → saludable  
• Aumenta contra tu dirección → peligro  

Si falta uno de los tres → no operas.
""")

# =========================================================
# 5️⃣ ENTRADA
# =========================================================

st.subheader("5️⃣ ENTRADA (El gatillo)")

st.markdown("""
No es cuando sientes.
Es cuando hay confirmación.

CALL:
• Cierre por encima del nivel  
• Retest que sostiene  
• Volumen comprador  

PUT:
• Rechazo claro  
• Cierre debajo del nivel  
• Volumen vendedor  

Timeframe ideal: 1–5 min.
""")

# =========================================================
# 6️⃣ INVALIDACIÓN
# =========================================================

st.subheader("6️⃣ INVALIDACIÓN")

st.markdown("""
Antes de entrar debes poder decir:

"Si el precio hace X, estoy equivocado."

Ejemplo:
Compras sobre VWAP.
Si cierra debajo con volumen → sales.

Sin discusión.
Sin esperanza.
""")

# =========================================================
# 7️⃣ STOP
# =========================================================

st.subheader("7️⃣ STOP")

st.markdown("""
Debe tener lógica estructural, no emocional.

Opciones:
• Debajo de la vela de entrada  
• Último swing  
• Nivel estructural perdido  

Para 0DTE:
Si no se mueve rápido a favor → sales.
El tiempo trabaja en contra.
""")

# =========================================================
# 8️⃣ TARGET
# =========================================================

st.subheader("8️⃣ TARGET")

st.markdown("""
Profesional:
Cobrar estructura.

Target 1 (obligatorio):
• VWAP  
• PDL  
• High del día  

Aquí:
Tomas parcial  
Mueves stop a Break Even  

Target 2:
Solo si hay estructura + volumen + espacio.
""")

# =========================================================
# 9️⃣ HIGH / LOW DEL DÍA
# =========================================================

st.subheader("9️⃣ HIGH / LOW DEL DÍA")

st.markdown("""
El primer impulso fuerte muchas veces marca:
• El máximo del día  
• O el mínimo del día  

Luego suele haber:
• Rango  
• Reversiones  
• Falsas rupturas  

Error común:
Perseguir el primer movimiento.

Profesional:
Esperar el retroceso.
""")
