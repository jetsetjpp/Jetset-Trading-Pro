### main.py — Jetset Trading Pro+ launcher with Firebase login and fixed config error

import streamlit as st
st.set_page_config(page_title="Jetset Trading Pro+", layout="wide")

from lang import get_language_dict
from risk_calculator import render_risk_tab
from journal import render_journal_tab
from performance import render_performance_tab
from auth import init_firebase, render_login_ui

# Initialize Firebase and render login UI
init_firebase()
render_login_ui()

# Block access if user not logged in
if "user" not in st.session_state:
    st.warning("🔒 Please log in to access the app.")
    st.stop()

# Language switcher
st.sidebar.markdown("🌍 **Language**")
language = st.sidebar.selectbox("", ["English", "Français"])
t = get_language_dict(language)

# App title
st.title("🚀 " + t["app_title"])

# Tabs
tabs = st.tabs([f"📊 {t['risk_tab']}", f"📓 {t['journal_tab']}", f"📈 {t['performance_tab']}"])

# Render each module
with tabs[0]:
    render_risk_tab(t)

with tabs[1]:
    render_journal_tab(t)

with tabs[2]:
    render_performance_tab(t)
