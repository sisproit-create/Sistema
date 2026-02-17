import streamlit as st

def init_session_state():

    defaults = {
        "permiso_operar": False,
        "mantra_activado": False,
        "checklist_percent": 0
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
