from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8769414302:AAHpS0oe7Rg1Rj9lRsn_2E4NkVt8oQ5JcCE"
VIDEO_BIZNES = "https://youtu.be/kMNRNFFF_wI"
FORM_LINK = "https://forms.gle/kLeUtvdVNAmphYid7"
ADMIN = "@abdulazizsaydaliyev"
ADMIN_ID = 1455425842
PHONE = "+998-99-640-44-66"

MEDIA_CHANNEL = -1004489946230
VIDEO_CANVAS = 3
VIDEO_AZIZ = 4
VIDEO_OZBEGIM = 5


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


async def biznes_flow(context: ContextTypes.DEFAULT_TYPE, chat_id: int, user):
    username = f"@{user.username}" if user.username else "username yo'q"

    # --- 1-xabar: YouTube video (darhol) ---
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Target orqali sotuv qilsa bo'ladimi ? Shu kabi barcha savollarga javob shu videoimizda !\n"
            "Amaranth mebel loyihamiz - 1 oyda $100,000 sotuv To'liq ko'rish uchun link orqali You tube kiring !\n\n"
            f"{VIDEO_BIZNES}"
        )
    )

    await asyncio.sleep(1 * 60)  # 30 daqiqa

    # --- 2-xabar: Natijalar + Uzqurilish ---
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Ko'pchilik biznes egalari targetdan natija chiqmaydi deb o'ylaydi\n\n"
            "Sababi oddiy — noto'g'ri strategiya noto'g'ri kreativ noto'g'ri auditoriya\n\n"
            "Biz boshqacha yondashamiz Mana natija:\n\n"
            "✅ Canvas.design — $1,000 reklama bilan $1,200 sotuv 4,000+ sifatli obunachi ROAS 12X\n"
            "✅ Aziz Uylar — $2,814 reklama bilan $6,000,000 lik uylar sotildi 10,000+ obunachi ROAS 6.4X\n"
            "✅ Amaranth Mebel — $2,000 reklama bilan $100,000 sotuv ROAS 50X\n\n"
            "Uzqurilish — O'zbekistondagi eng yirik ko'chmas mulk reklama agentliklaridan biri\n\n"
            "Biz bilan ishlashdan oldin 200,000 obunachi edi\n"
            "2 yil davomida 417,000 ga yetkazildi\n\n"
            "2 hafta ichida Telegramga 15,000+ sifatli obunachi qo'shildi\n"
            "Deyarli barcha videolari 100,000+ ko'rishga chiqdi\n"
            "131,490,113 marta ko'rinish — O'zbekiston auditoriyasini 2-3 marta aylanib chiqdik\n\n"
            "Kanal orqali sotilgan uylar — $10,000,000+\n\n"
            "Bu faqat target emas — to'g'ri strategiya va tizimli ish natijasi"
        )
    )

    await asyncio.sleep(1 * 60)  # 15 daqiqa

    # --- 3-xabar: Aziz Uylar otzyiv video ---
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Bu inson O'zbekistonda ko'chmas mulk bozorida taniqli ism — Aziz Uylar\n\n"
            "Bizning target reklamalarimiz orqali 2026 yilda $6,000,000 lik uylar sotildi\n\n"
            "3,062,164 odamga yetib bordik 10,000+ sifatli obunachi qo'shildi\n\n"
            "Aziz o'zi aytib beradi 👇"
        )
    )
    await context.bot.forward_message(
        chat_id=chat_id,
        from_chat_id=MEDIA_CHANNEL,
        message_id=VIDEO_AZIZ
    )

    await asyncio.sleep(1 * 60)  # 15 daqiqa

    # --- 4-xabar: Canvas.design otzyiv video ---
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Arxitektura va interier dizayn biznesida ham target ishlaydi\n\n"
            "$1,000 reklama bilan $1,200 sotuv va 4,000+ sifatli obunachi\n\n"
            "Mijozimiz o'zi aytib beradi 👇"
        )
    )
    await context.bot.forward_message(
        chat_id=chat_id,
        from_chat_id=MEDIA_CHANNEL,
        message_id=VIDEO_CANVAS
    )

    await asyncio.sleep(1 * 60)  # 15 daqiqa

    # --- 5-xabar: O'zbegim otzyiv video ---
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Kiyim-kechak biznesida ham target ishlaydi\n\n"
            "Muhim narsa — to'g'ri auditoriya va to'g'ri kreativ\n\n"
            "Mijozimiz tajribasini o'zi aytib beradi 👇"
        )
    )
    await context.bot.forward_message(
        chat_id=chat_id,
        from_chat_id=MEDIA_CHANNEL,
        message_id=VIDEO_OZBEGIM
    )

    await asyncio.sleep(1 * 60)  # 30 daqiqa

    # --- 6-xabar: Taklif ---
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Siz ham biznesingizni o'sishini xohlaysizmi ?\n\n"
            "Har oy faqat cheklangan miqdorda yangi loyiha qabul qilamiz — chunki har bir loyihaga to'liq e'tibor beramiz\n\n"
            "Hozir bo'sh joy bor\n\n"
            "👇 Bepul konsultatsiyaga yoziling — biznesingizni tahlil qilib qayerdan boshlash kerakligini aytib beramiz:\n\n"
            f"{FORM_LINK}\n\n"
            f"📞 {PHONE}\n"
            f"✍️ {ADMIN}"
        )
    )

    if ADMIN_ID:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"✅ {user.full_name} ({username}) — to'liq funnel tugadi form yuborildi"
        )


async def targetchi_flow(context: ContextTypes.DEFAULT_TYPE, chat_id: int, user):
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Target orqali sotuv qilsa bo'ladimi ? Shu kabi barcha savollarga javob shu videoimizda !\n"
            "Amaranth mebel loyihamiz - 1 oyda $100,000 sotuv To'liq ko'rish uchun link orqali You tube kiring !\n\n"
            f"{VIDEO_BIZNES}\n\n"
            f"Savollar bo'lsa yozing 👉 {ADMIN}"
        )
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
        await query.edit_message_text("Zo'r! Hozir yuboramiz 👇")
        asyncio.create_task(biznes_flow(context, chat_id, user))

    elif query.data == "targetchi":
        if ADMIN_ID:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"✅ {user.full_name} ({username}) — Targetolog tugmasini bosdi"
            )
        await query.edit_message_text("Zo'r! Hozir yuboramiz 👇")
        asyncio.create_task(targetchi_flow(context, chat_id, user))


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sizning ID: `{update.effective_user.id}`", parse_mode="Markdown")


if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot ishga tushdi ✅")
    app.run_polling(drop_pending_updates=True)
