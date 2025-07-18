from app.bot.whatsapp_twilio import app

if __name__ == "__main__":
    print("Twilio WhatsApp Bot başlatılıyor...")
    print("Bot http://localhost:5000 adresinde çalışıyor")
    print("Webhook URL: http://localhost:5000/webhook")
    print("\nKURULUM ADIMLARI:")
    print("1. https://www.twilio.com/try-twilio adresine gidin")
    print("2. Ücretsiz hesap oluşturun")
    print("3. WhatsApp Sandbox'ı aktifleştirin")
    print("4. Webhook URL'ini Twilio'ya ekleyin")
    print("5. .env dosyasına Twilio bilgilerini ekleyin")
    app.run(host='0.0.0.0', port=5000, debug=True) 