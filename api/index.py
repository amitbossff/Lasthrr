from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import urllib.parse
import os
import json

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to last hour bot send your search tag"
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = urllib.parse.quote(update.message.text)
    link = f"https://www.youtube.com/results?search_query={query}&sp=EgIIAQ%3D%3D"
    await update.message.reply_text(link)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

async def handler(request, context):
    body = await request.json()
    update = Update.de_json(body, app.bot)
    await app.process_update(update)
    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True})
    }
