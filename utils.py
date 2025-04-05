import os
from datetime import datetime
import streamlit as st
import pandas as pd

# Save screenshot to disk and return the path
def save_screenshot(file):
    if file is None:
        return ""
    os.makedirs("Screenshots", exist_ok=True)
    filename = f"Screenshots/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.name}"
    with open(filename, "wb") as f:
        f.write(file.getbuffer())
    return filename

# Basic sentiment detection from notes
def detect_sentiment(notes: str):
    notes = notes.lower()
    if "confident" in notes or "confiance" in notes:
        return "🔥 Confident"
    elif "nervous" in notes or "peur" in notes or "stressé" in notes:
        return "😬 Hesitant"
    return "🧘 Neutral"

# Calculate profit or loss
def calculate_pnl(entry, exit, qty, fees, trade_type):
    pnl = (exit - entry) * qty - fees if trade_type.lower() in ["buy", "achat"] else (entry - exit) * qty - fees
    return round(pnl, 2)

# Show screenshot preview
def render_image(path):
    if path and os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.info("No screenshot available.")



# Import trades from Excel
def import_trades(file):
    df = pd.read_excel(file)
    df.fillna("", inplace=True)
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    return df

# Export trades to Excel
def export_trades(df):
    from io import BytesIO
    df["Date"] = df["Date"].astype(str)
    excel = BytesIO()
    df.to_excel(excel, index=False)
    return excel.getvalue()
