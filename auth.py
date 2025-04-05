### auth.py — Firebase Email/Password Admin Auth (admin login only)

import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import json

# ✅ Initialize Firebase Admin SDK once using Streamlit secrets
def init_firebase():
    if "firebase_app" not in st.session_state:
        # Load credentials from Streamlit secrets
        cred_info = st.secrets["firebase_service_account"]
        cred = credentials.Certificate(json.loads(cred_info.to_json()))
        firebase_admin.initialize_app(cred)
        st.session_state["firebase_app"] = True

# ✅ Create a new user (admin sign-up only)
def sign_up_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return f"✅ User created: {user.uid}"
    except Exception as e:
        return f"❌ {e}"

# ✅ TEMPORARY Admin Login System
admin_users = {
    "admin@example.com": "adminpass"  # Replace or load from a file later
}

def login_admin(email, password):
    if email in admin_users and password == admin_users[email]:
        st.session_state["user"] = email
        return True
    return False

# ✅ Streamlit Login UI (called from main.py)
def render_login_ui():
    st.sidebar.header("🔐 Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login_admin(email, password):
            st.sidebar.success(f"✅ Logged in as {email}")
        else:
            st.sidebar.error("❌ Invalid credentials")

    st.sidebar.markdown("---")
    st.sidebar.subheader("🆕 Sign Up")
    new_email = st.sidebar.text_input("New Email", key="new_email")
    new_pw = st.sidebar.text_input("New Password", type="password", key="new_pw")
    if st.sidebar.button("Create Account"):
        msg = sign_up_user(new_email, new_pw)
        st.sidebar.info(msg)
