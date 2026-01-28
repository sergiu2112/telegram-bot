import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
        [InlineKeyboardButton("⚙️ Setări", callback_data="setari")],
        [InlineKeyboardButton("❌ Închide", callback_data="inchide")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Salut 👋\nAlege o opțiune din meniu:",
        reply_markup=reply_markup,
    )

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text("ℹ️ Acesta este un bot Telegram demo.")
    elif query.data == "setari":
        await query.edit_message_text("⚙️ Setările nu sunt încă disponibile.")
    elif query.data == "inchide":
        await query.edit_message_text("❌ Meniu închis.")

def main():
    if not TOKEN:
        raise ValueError("TOKEN nu este setat în variabilele de mediu")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Botul rulează...")
    app.run_polling()

if name == "__main__":
    main()
