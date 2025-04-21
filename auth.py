import streamlit as st
import pyrebase

firebase_config = {
    "apiKey": st.secrets["firebase_api_key"],
    "authDomain": st.secrets["firebase_auth_domain"],
    "projectId": st.secrets["firebase_project_id"],
    "storageBucket": st.secrets["firebase_storage_bucket"],
    "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
    "appId": st.secrets["firebase_app_id"],
    "measurementId": st.secrets["firebase_measurement_id"],
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_ui():
    st.title("🔐 Login to Jetset Trading Pro+")
    choice = st.selectbox("Login or Sign Up", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Login":
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state["user"] = user
                st.success("Logged in successfully!")
                st.experimental_rerun()
            except:
                st.error("Login failed. Please check your credentials.")
    else:
        if st.button("Create Account"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully. You can now log in.")
            except:
                st.error("Account creation failed. Try a different email.")

def is_logged_in():
    return "user" in st.session_state

def logout_button():
    if st.button("Logout"):
        st.session_state.pop("user", None)
        st.experimental_rerun()
