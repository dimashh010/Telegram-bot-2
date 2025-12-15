from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Сәлем!\nҚызмет алу үшін /buy деп жазыңыз"
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Қызмет 1", callback_data="service_1")],
        [InlineKeyboardButton("Қызмет 2", callback_data="service_2")]
    ]
    await update.message.reply_text(
        "🛒 Қызметті таңдаңыз:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    total = 1000 if query.data == "service_1" else 2000

    keyboard = [
        [
            InlineKeyboardButton("Kaspi", callback_data="kaspi"),
            InlineKeyboardButton("Halyk", callback_data="halyk")
        ]
    ]

    await query.message.reply_text(
        f"💰 Төлем: {total} тг\nТөлем әдісін таңдаңыз 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "kaspi":
        await query.message.reply_text("📲 Kaspi арқылы төлеңіз")
    elif query.data == "halyk":
        await query.message.reply_text("💳 Halyk арқылы төлеңіз")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CallbackQueryHandler(services, pattern="service_"))
    app.add_handler(CallbackQueryHandler(payment, pattern="kaspi|halyk"))

    print("🤖 Bot started (Railway)")
    app.run_polling()

if __name__ == "__main__":
    main()
