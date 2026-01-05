from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8011220850:AAEXRvY4RQDLtPWpsYXcORmrdlVOJ9C3Wrw"

WELCOME_TEXT = """
✦ Welcome to COSMOS 🌌 ✦

A quiet universe awaits you.
Speak gently. Observe deeply.

— ✦
"""

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(WELCOME_TEXT)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

app.run_polling()
