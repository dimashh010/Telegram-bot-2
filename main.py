import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("8138330264:AAFqUx3kqrFg0SnusjhujE0IBdX_BB9WfC0")

async def start(update, context):
    await update.message.reply_text("Бот жұмыс істеп тұр ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
