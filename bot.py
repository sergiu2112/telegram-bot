import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Info", callback_data="info")],
        [InlineKeyboardButton("⚙️ Setări", callback_data="setari")],
        [InlineKeyboardButton("❌ Închide", callback_data="inchide")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Salut 👋\nAlege o opțiune:",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text("📊 Informații bot")

    elif query.data == "setari":
        await query.edit_message_text("⚙️ Setări")

    elif query.data == "inchide":
        await query.edit_message_text("❌ Meniu închis")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()

if name == "__main__":
    main()
