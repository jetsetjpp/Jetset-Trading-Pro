import streamlit as st
from google.cloud import firestore

def get_firestore_client():
    if "firestore_client" not in st.session_state:
        st.session_state.firestore_client = firestore.Client.from_service_account_json(
            "firebase_config/serviceAccountKey.json"
        )
    return st.session_state.firestore_client

def save_user_trades(email, trades_df):
    db = get_firestore_client()
    doc_ref = db.collection("trades").document(email)
    doc_ref.set({"trades": trades_df.to_dict(orient="records")})

def load_user_trades(email):
    db = get_firestore_client()
    doc_ref = db.collection("trades").document(email).get()
    if doc_ref.exists:
        records = doc_ref.to_dict().get("trades", [])
        return records
    return []
