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
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
        [InlineKeyboardButton("⚙️ Setări", callback_data="setari")],
        [InlineKeyboardButton("❌ Închide", callback_data="inchide")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Salut! Alege o opțiune din meniu:",
        reply_markup=reply_markup,
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text("ℹ️ Acesta este un bot demo.")
    elif query.data == "setari":
        await query.edit_message_text("⚙️ Setările nu sunt încă disponibile.")
    elif query.data == "inchide":
        await query.edit_message_text("❌ Meniul a fost închis.")


def main():
    if not TOKEN:
        raise RuntimeError("TOKEN nu este setat în Environment Variables")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("🤖 Botul rulează...")
    app.run_polling()


if __name__== "__main__":
    main()
