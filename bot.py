import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# === SOZLAMALAR ===
BOT_TOKEN = "8769414302:AAHpS0oe7Rg1Rj9lRsn_2E4NkVt8oQ5JcCE"

VIDEO_BIZNES = "https://youtu.be/kMNRNFFF_wI"
VIDEO_TARGETCHI = "https://youtu.be/kMNRNFFF_wI"  # Keyinroq almashtiring

ADMIN_USERNAME = "@Abdul.saydal"

# === LOGGING ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏢 Men biznes egasiman", callback_data="biznes")],
        [InlineKeyboardButton("🎯 Men targetchi/SMM mutaxassisiman", callback_data="targetchi")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\n"
        "Siz kim bo'lasiz?",
        reply_markup=reply_markup
    )


# === TUGMA BOSILGANDA ===
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "biznes":
        await query.edit_message_text(
            "Ajoyib! 💼\n\n"
            "Targetdan haqiqatan ham sotuvlar bo'ladimi?\n"
            "Natijalar real bo'ladimi?\n\n"
            "Mijozlarimizning o'zlari javob bersin 👇\n\n"
            f"🎬 {VIDEO_BIZNES}\n\n"
            "Videoni ko'rib bo'lgach, biz bilan ishlashni xohlasangiz — "
            f"murojaat qiling: {ADMIN_USERNAME}"
        )

    elif query.data == "targetchi":
        await query.edit_message_text(
            "Zo'r! 🎯\n\n"
            "Targeting bo'yicha daromadingizni oshirishni xohlaysizmi?\n"
            "Mijozlar bilan natija chiqarishni o'rganmoqchimisiz?\n\n"
            "Ushbu videoda hamma narsa bor 👇\n\n"
            f"🎬 {VIDEO_TARGETCHI}\n\n"
            f"Savollar bo'lsa — murojaat qiling: {ADMIN_USERNAME}"
        )


# === MAIN ===
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot ishga tushdi ✅")
    app.run_polling()


if __name__ == "__main__":
    main()
