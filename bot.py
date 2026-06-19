from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8769414302:AAHpS0oe7Rg1Rj9lRsn_2E4NkVt8oQ5JcCE"
VIDEO_BIZNES = "https://youtu.be/kMNRNFFF_wI"
VIDEO_TARGETCHI = "https://youtu.be/kMNRNFFF_wI"
ADMIN = "@Abdul.saydal"
ADMIN_ID = 1455425842


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.full_name
    username = f"@{user.username}" if user.username else "username yo'q"

    # Admin ga xabar yuborish
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

    if query.data == "biznes":
        # Admin ga tanlov xabari
        if ADMIN_ID:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"✅ {user.full_name} ({username}) — Biznes egasi tugmasini bosdi"
            )
        await query.edit_message_text(
            "Mebel biznesida 1 oyda $100,000 sotuv qilgan mijozimiz targeting haqida o'zi gapirib beradi 👇\n\n"
            f"{VIDEO_BIZNES}\n\n"
            f"Biz bilan ishlashni xohlasangiz, murojaat qiling 👉 {ADMIN}"
        )

    elif query.data == "targetchi":
        if ADMIN_ID:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"✅ {user.full_name} ({username}) — Targetolog tugmasini bosdi"
            )
        await query.edit_message_text(
            "Targeting orqali mijozlar uchun real natija chiqarish va o'z daromadingizni oshirish haqida to'liq ma'lumot 👇\n\n"
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
