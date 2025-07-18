from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from app.api.price_api import get_current_price
from app.bot.price_manager import set_price
from app.config.admin_config import is_whatsapp_admin
import os
from dotenv import load_dotenv
import requests


def ask_ai_openrouter(message):
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",  # veya başka bir model ismi
        "messages": [
            {"role": "user", "content": message}
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Üzgünüm, şu anda yardımcı olamıyorum."

# Environment dosyasını yükle
load_dotenv()

app = Flask(__name__)

# Twilio bilgileri (environment dosyasından)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', 'whatsapp:+14155238886')

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Twilio WhatsApp webhook endpoint'i
    """
    # Gelen mesajı al
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')  # whatsapp:+905551234567 formatında
    
    print(f"Gelen mesaj: {incoming_msg} - Kimden: {from_number}")
    
    # Mesajı işle
    response_text = handle_message(incoming_msg, from_number)
    
    # TwiML yanıtı oluştur
    resp = MessagingResponse()
    resp.message(response_text)
    
    return str(resp)

def handle_message(message: str, phone_number: str) -> str:
    """
    Gelen mesajı işler ve uygun yanıtı döner
    """
    # /start komutu
    if message.lower() in ['/start', 'start', 'hey', 'hi', 'hello', 'merhaba']:
        return (
            "Yapmak istediğiniz işlemi seçiniz:\n"
            "1) Güncel demir fiyatı öğrenme\n"
            "2) Belirtilen kg için toplam fiyat hesaplama\n\n"
            "Yönetici komutları:\n"
            "/setprice [fiyat] - Fiyat güncelleme"
        )
    
    # /setprice komutu kontrolü
    if message.startswith('/setprice'):
        if not is_whatsapp_admin(phone_number):
            return "Bu komutu sadece yöneticiler kullanabilir."
        
        try:
            parts = message.split()
            if len(parts) != 2:
                return "Lütfen geçerli bir fiyat girin. Örn: /setprice 48.75"
            
            new_price = parts[1]
            set_price(new_price)
            return f"Yeni fiyat {new_price} olarak kaydedildi."
        except:
            return "Lütfen geçerli bir fiyat girin. Örn: /setprice 48.75"
    
    # Normal mesaj işleme
    if message == "1":
        price_info = get_current_price()
        if price_info:
            return f"Güncel demir fiyatı: {price_info['price_per_kg']} {price_info['currency']}"
        else:
            return "Fiyatlar henüz açıklanmadı."
    
    elif message == "2":
        return "Kaç kg demir için fiyat hesaplayalım?\n\nLütfen kg miktarını yazın (örn: 5, 10.5, 25)"
    
    elif message.replace(".", "", 1).isdigit():
        price_info = get_current_price()
        if price_info:
            kg = float(message)
            total_price = price_info["price_per_kg"] * kg
            return f"{kg} kg demir için toplam fiyat: {total_price:.2f} {price_info['currency']}"
        else:
            return "Fiyatlar henüz açıklanmadı."
    
    else:
        ai_response = ask_ai_openrouter(message)
        return ai_response

@app.route('/start', methods=['GET'])
def start():
    """
    Bot başlatma endpoint'i
    """
    return "Twilio WhatsApp Bot çalışıyor..."

if __name__ == '__main__':
    app.run(debug=True, port=5000) 