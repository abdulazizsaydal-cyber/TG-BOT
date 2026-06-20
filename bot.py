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

active_users = set()


async def send(bot, chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else "username yo'q"
    if ADMIN_ID:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 Yangi foydalanuvchi!\n\n👤 Ism: {user.full_name}\n📱 Username: {username}\n🆔 ID: {user.id}"
        )
    keyboard = [
        [InlineKeyboardButton("🏢 Biznes egasi", callback_data="biznes")],
        [InlineKeyboardButton("🎯 Targetolog / Marketolog", callback_data="targetchi")],
    ]
    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\nSiz kim bo'lasiz?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def biznes_flow(bot, chat_id, user):
    username = f"@{user.username}" if user.username else "username yo'q"

    # 1 — YouTube video (preview yoqiq)
    await bot.send_message(
        chat_id=chat_id,
        text=(
            "Target orqali sotuv qilsa bo'ladimi ? Shu kabi barcha savollarga javob shu videoimizda !\n"
            "Amaranth mebel loyihamiz - 1 oyda $100,000 sotuv To'liq ko'rish uchun link orqali You tube kiring !\n\n"
            f"{VIDEO_BIZNES}"
        )
    )

    await asyncio.sleep(30)

    # 2 — Umumiy natijalar
    await send(bot, chat_id,
        "Ko'pchilik biznes egalari targetga pul sarflaydi — natija ko'rmaydi\n\n"
        "Sababi oddiy — noto'g'ri strategiya noto'g'ri kreativ noto'g'ri auditoriya\n\n"
        "Biz boshqacha yondashamiz Mana haqiqiy natijalar:\n\n"
        "✅ Canvas design — $1,000 reklama bilan $12,000 sotuv 4,000+ sifatli obunachi ROAS 12X\n"
        "✅ Aziz Uylar — $2,814 reklama bilan $6,000,000 lik uylar sotildi 10,000+ obunachi\n"
        "✅ Amaranth Mebel — $2,000 reklama bilan $100,000 sotuv ROAS 50X\n"
        "✅ Uzqurilish — 2 hafta ichida 15,000+ Telegram obunachi 131 mln+ ko'rinish $10,000,000+ sotuv\n\n"
        f"👇 Bepul konsultatsiyaga yoziling:\n{FORM_LINK}"
    )

    await asyncio.sleep(30)

    # 3 — Uzqurilish
    await send(bot, chat_id,
        "Uzqurilish — O'zbekistondagi eng yirik ko'chmas mulk reklama agentliklaridan biri\n\n"
        "Biz bilan ishlashdan oldin 200,000 obunachi edi — 2 yilda 417,000 ga yetkazildi\n\n"
        "2 hafta ichida Telegramga 15,000+ sifatli obunachi qo'shildi\n"
        "Barcha videolari 100,000+ ko'rishga chiqdi\n"
        "131,490,113 marta ko'rinish — O'zbekiston auditoriyasini 2-3 marta aylanib chiqdik\n\n"
        "Kanal orqali sotilgan uylar — $10,000,000+\n\n"
        "Bu faqat reklama emas — to'g'ri strategiya tizimli ish va har bir loyihaga alohida yondashuv natijasi\n\n"
        f"👇 Bepul konsultatsiyaga yoziling:\n{FORM_LINK}"
    )

    await asyncio.sleep(30)

    # 4 — Aziz Uylar
    await send(bot, chat_id,
        "Bu inson O'zbekistonda ko'chmas mulk bozorida taniqli ism — Aziz Uylar\n\n"
        "Bizning target reklamalarimiz orqali 2026 yilda $6,000,000 lik uylar sotildi\n\n"
        "3,062,164 odamga yetib bordik 10,000+ sifatli obunachi qo'shildi\n\n"
        "Aziz o'zi aytib beradi 👇"
    )
    await bot.forward_message(chat_id=chat_id, from_chat_id=MEDIA_CHANNEL, message_id=VIDEO_AZIZ)
    await send(bot, chat_id, f"👇 Bepul konsultatsiyaga yoziling:\n{FORM_LINK}")

    await asyncio.sleep(30)

    # 5 — Canvas.design
    await send(bot, chat_id,
        "Arxitektura va interier dizayn — raqobat qattiq nisha\n\n"
        "Shunga qaramay $1,000 reklama bilan $12,000 sotuv va 4,000+ sifatli obunachi yig'ildi\n"
        "To'g'ri kreativ to'g'ri auditoriya — natija o'zi keladi\n\n"
        "Mijozimiz o'zi gapirib beradi 👇"
    )
    await bot.forward_message(chat_id=chat_id, from_chat_id=MEDIA_CHANNEL, message_id=VIDEO_CANVAS)
    await send(bot, chat_id, f"👇 Bepul konsultatsiyaga yoziling:\n{FORM_LINK}")

    await asyncio.sleep(30)

    # 6 — O'zbegim
    await send(bot, chat_id,
        "Kiyim-kechak biznesida raqobat ko'p — lekin to'g'ri target bilan ajralib chiqish mumkin\n\n"
        "Aynan shu biznesda ham biz natija chiqardik\n"
        "Xaridorlar keldi sotuvlar o'sdi brend taniqli bo'ldi\n\n"
        "Mijozimiz tajribasini o'zi aytib beradi 👇"
    )
    await bot.forward_message(chat_id=chat_id, from_chat_id=MEDIA_CHANNEL, message_id=VIDEO_OZBEGIM)
    await send(bot, chat_id, f"👇 Bepul konsultatsiyaga yoziling:\n{FORM_LINK}")

    await asyncio.sleep(30)

    # 7 — Yakuniy taklif
    await send(bot, chat_id,
        "Siz ham biznesingizni o'sishini xohlaysizmi ?\n\n"
        "Har oy faqat cheklangan miqdorda yangi loyiha qabul qilamiz — chunki har bir loyihaga to'liq e'tibor beramiz\n\n"
        "Hozir bo'sh joy bor\n\n"
        "👇 Bepul konsultatsiyaga yoziling — biznesingizni tahlil qilib qayerdan boshlash kerakligini aytib beramiz:\n\n"
        f"{FORM_LINK}\n\n"
        f"📞 {PHONE}\n"
        f"✍️ {ADMIN}"
    )

    if ADMIN_ID:
        await bot.send_message(chat_id=ADMIN_ID, text=f"✅ {user.full_name} ({username}) — to'liq funnel tugadi")

    active_users.discard(chat_id)


async def targetchi_flow(bot, chat_id, user):
    await send(bot, chat_id,
        "Target orqali sotuv qilsa bo'ladimi ? Shu kabi barcha savollarga javob shu videoimizda !\n"
        "Amaranth mebel loyihamiz - 1 oyda $100,000 sotuv To'liq ko'rish uchun link orqali You tube kiring !\n\n"
        f"{VIDEO_BIZNES}\n\n"
        f"Savollar bo'lsa yozing 👉 {ADMIN}"
    )
    active_users.discard(chat_id)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    username = f"@{user.username}" if user.username else "username yo'q"
    chat_id = query.message.chat_id

    if chat_id in active_users:
        return
    active_users.add(chat_id)

    if query.data == "biznes":
        if ADMIN_ID:
            await context.bot.send_message(chat_id=ADMIN_ID, text=f"✅ {user.full_name} ({username}) — Biznes egasi tugmasini bosdi")
        await query.edit_message_text("Zo'r! Hozir yuboramiz 👇")
        asyncio.ensure_future(biznes_flow(context.bot, chat_id, user))

    elif query.data == "targetchi":
        if ADMIN_ID:
            await context.bot.send_message(chat_id=ADMIN_ID, text=f"✅ {user.full_name} ({username}) — Targetolog tugmasini bosdi")
        await query.edit_message_text("Zo'r! Hozir yuboramiz 👇")
        asyncio.ensure_future(targetchi_flow(context.bot, chat_id, user))


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sizning ID: `{update.effective_user.id}`", parse_mode="Markdown")


if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot ishga tushdi ✅")
    app.run_polling(drop_pending_updates=True)
