from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

app = Flask(__name__)

# Initialize Firebase Admin
cred = credentials.Certificate("firebase_config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Optional secret key to prevent spam
SECRET_KEY = "jetset_secret_123"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    if data.get("secret") != SECRET_KEY:
        return jsonify({"error": "Invalid secret key"}), 403

    required = ["email", "ticker", "type", "entry", "stop", "tp1", "qty", "strategy", "tag"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    trade = {
        "Date": datetime.date.today().isoformat(),
        "Time": datetime.datetime.now().strftime("%H:%M"),
        "Ticker": data["ticker"],
        "Type": data["type"],
        "Entry": float(data["entry"]),
        "Stop": float(data["stop"]),
        "TP1": float(data["tp1"]),
        "TP2": float(data.get("tp2", 0)),
        "Exit": 0.0,
        "Qty": int(data["qty"]),
        "Fees": float(data.get("fees", 0)),
        "Strategy": data["strategy"],
        "Notes": data.get("notes", ""),
        "Tag": data["tag"],
        "Sentiment": "📡 Auto",
        "Screenshot": "",
        "P&L": 0.0
    }

    email = data["email"]
    doc_ref = db.collection("trades").document(email)
    existing = doc_ref.get().to_dict()
    trades = existing["trades"] if existing and "trades" in existing else []
    trades.append(trade)
    doc_ref.set({"trades": trades})

    return jsonify({"success": True, "message": "Trade logged!"})

# 🔥 Run the app
if __name__ == '__main__':
    app.run(port=5000)

