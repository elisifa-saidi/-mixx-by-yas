from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

BOT_TOKEN = os.environ.get("7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0")
CHAT_ID = os.environ.get("6958413637")

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/submit-loan", methods=["POST"])
def submit_loan():

    data = request.get_json()

    name = data.get("name")
    phone = data.get("phone")
    loan_amount = data.get("loan_amount")

    ujumbe = f"""
NEW LOAN APPLICATION

Name: {name}
Phone: {phone}
Loan Amount: {loan_amount}
"""

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        telegram_url,
        json={
            "chat_id": CHAT_ID,
            "text": ujumbe
        }
    )

    print(response.text)

    if response.status_code == 200:

        return jsonify({
            "message":"Application sent successfully"
        })

    else:

        return jsonify({
            "message":"Telegram failed"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
