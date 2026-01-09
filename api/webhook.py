import os
import json
import urllib.parse
import requests

TOKEN = os.environ.get("BOT_TOKEN")

def handler(request):
    try:
        raw = request.body.decode("utf-8")
        data = json.loads(raw)

        message = data.get("message")
        if not message:
            return "ok"

        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            reply = "Welcome to last hour bot send your search tag"
        else:
            query = urllib.parse.quote(text)
            reply = f"https://www.youtube.com/results?search_query={query}&sp=EgIIAQ%3D%3D"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={
            "chat_id": chat_id,
            "text": reply
        }, timeout=5)

        return "ok"

    except Exception as e:
        return str(e)
