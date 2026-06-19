from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8769414302:AAHpS0oe7Rg1Rj9lRsn_2E4NkVt8oQ5JcCE"
VIDEO_BIZNES = "https://youtu.be/kMNRNFFF_wI"
VIDEO_TARGETCHI = "https://youtu.be/kMNRNFFF_wI"
FORM_LINK = "https://forms.gle/kLeUtvdVNAmphYid7"
ADMIN = "@abdulazizsaydaliyev"
ADMIN_ID = 1455425842

DELAY_SECONDS = 30 * 60  # 30 daqiqa


async def send_form_later(context: ContextTypes.DEFAULT_TYPE, chat_id: int):
    await asyncio.sleep(DELAY_SECONDS)
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Target xizmatimiz orqali siz ham mijozlaringiz oqimini oshiring!\n\n"
            "📌 Joylar soni cheklangan — ulgurib qoling.\n"
            "Ro'yxatdan o'ting va bepul konsultatsiyaga ega bo'ling 👇\n\n"
            f"{FORM_LINK}"
        )
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.full_name
    username = f"@{user.username}" if user.username else "username yo'q"

    if ADMIN_ID:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 Yangi foydalanuvchi!\n\n👤 Ism: {name}\n📱 Username: {username}\n🆔 ID: {user.id}"
        )

    keyboard = [
        [InlineKeyboardButton("🏢 Biznes egasi", callback_data="biznes")],
        [InlineKeyboardButton("🎯 Targetolog / Marketolog", callback_data="targetchi")],
    ]
    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\nSiz kim bo'lasiz?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    username = f"@{user.username}" if user.username else "username yo'q"
    chat_id = query.message.chat_id

    if query.data == "biznes":
        if ADMIN_ID:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"✅ {user.full_name} ({username}) — Biznes egasi tugmasini bosdi"
            )

        await query.edit_message_text(
            "Target orqali sotuv qilsa bo'ladimi? Shu kabi barcha savollarga javob shu videoimizda!\n\nAmaranth mebel loyihamiz — 1 oyda $100,000 sotuv 🔥\n\nTo'liq ko'rish uchun link orqali YouTube ga kiring 👇\n\n"
            f"{VIDEO_BIZNES}"
        )

        # 30 daqiqadan keyin form yuborish
        asyncio.create_task(send_form_later(context, chat_id))

    elif query.data == "targetchi":
        if ADMIN_ID:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"✅ {user.full_name} ({username}) — Targetolog tugmasini bosdi"
            )

        await query.edit_message_text(
            "Target orqali sotuv qilsa bo'ladimi? Shu kabi barcha savollarga javob shu videoimizda!\n\nAmaranth mebel loyihamiz — 1 oyda $100,000 sotuv 🔥\n\nTo'liq ko'rish uchun link orqali YouTube ga kiring 👇\n\n"
            f"{VIDEO_TARGETCHI}\n\n"
            f"Savollar bo'lsa, yozing 👉 {ADMIN}"
        )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sizning ID: `{update.effective_user.id}`", parse_mode="Markdown")


if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot ishga tushdi ✅")
    app.run_polling(drop_pending_updates=True)
