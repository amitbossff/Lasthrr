import os
import json
import urllib.parse
import requests

TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

def handler(request):
    try:
        body = json.loads(request.body)

        message = body.get("message")
        if not message:
            return {"statusCode": 200, "body": "no message"}

        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            send_message(chat_id, "Welcome to last hour bot send your search tag")
        else:
            query = urllib.parse.quote(text)
            link = f"https://www.youtube.com/results?search_query={query}&sp=EgIIAQ%3D%3D"
            send_message(chat_id, link)

        return {"statusCode": 200, "body": "ok"}

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
            }
