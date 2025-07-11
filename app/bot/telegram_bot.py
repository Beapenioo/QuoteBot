from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from app.api.price_api import get_current_price
from app.bot.price_manager import set_price

TOKEN = "7718245640:AAG17vghr99lLCCgAHDEHkhoTiNW--qB_IA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Yapmak istediğiniz işlemi seçiniz:\n"
        "1) Güncel demir fiyatı öğrenme\n"
        "2) Belirtilen kg için toplam fiyat hesaplama\n"
        "Fiyat güncellemesi için: /setprice 50.5"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.strip()

    if message == "1":
        price_info = get_current_price()
        if price_info:
            await update.message.reply_text(f"Güncel demir fiyatı: {price_info['price_per_kg']} {price_info['currency']}")
        else:
            await update.message.reply_text("Fiyatlar henüz açıklanmadı.")

    elif message == "2":
        await update.message.reply_text("Kaç kg demir için fiyat hesaplayalım?")

    elif message.replace(".", "", 1).isdigit():
        price_info = get_current_price()
        if price_info:
            kg = float(message)
            total_price = price_info["price_per_kg"] * kg
            await update.message.reply_text(f"{kg} kg demir için toplam fiyat: {total_price:.2f} {price_info['currency']}")
        else:
            await update.message.reply_text("Fiyatlar henüz açıklanmadı.")

    else:
        await update.message.reply_text("Geçersiz seçim.")

async def set_price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        new_price = context.args[0]
        set_price(new_price)
        await update.message.reply_text(f"Yeni fiyat {new_price} olarak kaydedildi.")
    except:
        await update.message.reply_text("Lütfen geçerli bir fiyat girin. Örn: /setprice 48.75")

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setprice", set_price_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot çalışıyor...")
    app.run_polling()
