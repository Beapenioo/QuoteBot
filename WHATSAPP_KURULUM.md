# WhatsApp Bot Kurulum Rehberi (Ücretsiz)

## 1. Twilio Hesabı Oluşturma

### Adım 1: Twilio'ya Kayıt Olun
- https://www.twilio.com/try-twilio adresine gidin
- Ücretsiz hesap oluşturun (kredi kartı gerekmez)
- E-posta doğrulamasını tamamlayın

### Adım 2: WhatsApp Sandbox'ı Aktifleştirin
1. Twilio Console'da **Messaging** > **Try it out** > **Send a WhatsApp message**
2. **Join the sandbox** butonuna tıklayın
3. WhatsApp'ta verilen kodu gönderin
4. Sandbox numarasını not edin: `+14155238886`

### Adım 3: Twilio Bilgilerini Alın
1. Console'da **Account Info** bölümünden:
   - **Account SID**'yi kopyalayın
   - **Auth Token**'ı kopyalayın

## 2. Bot Kurulumu

### Adım 1: Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 2: Environment Dosyası Oluşturun
1. `env_example.txt` dosyasını `.env` olarak kopyalayın
2. `.env` dosyasını düzenleyin:
```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=whatsapp:+14155238886
```

### Adım 3: Yönetici Bilgilerini Güncelleyin
`app/config/admin_config.py` dosyasında:
```python
WHATSAPP_ADMIN_PHONES = [
    "whatsapp:+905417189074",  
]
```

### Adım 4: Bot'u Başlatın
```bash
python run_twilio_whatsapp.py
```

## 3. Webhook Kurulumu

### Adım 1: ngrok Kurulumu (Ücretsiz)
1. https://ngrok.com/ adresinden ngrok indirin
2. Ücretsiz hesap oluşturun
3. Auth token'ı alın ve ngrok'u yapılandırın

### Adım 2: ngrok Başlatın
```bash
ngrok http 5000
```

### Adım 3: Webhook URL'ini Twilio'ya Ekleyin
1. ngrok'tan aldığınız URL'yi kopyalayın (örn: https://abc123.ngrok.io)
2. Twilio Console'da **Messaging** > **Settings** > **Webhook**
3. **Webhook URL**'e şunu ekleyin: `https://abc123.ngrok.io/webhook`

## 4. Test Etme

### Adım 1: WhatsApp'ta Test
1. WhatsApp'ta Twilio sandbox numarasına mesaj gönderin
2. Bot yanıt verecektir

### Adım 2: Yönetici Komutları
- `/setprice 50.5` - Fiyat güncelleme (sadece yöneticiler)

## Sorun Giderme

### Bot Yanıt Vermiyor
- ngrok URL'sinin doğru olduğundan emin olun
- Twilio webhook URL'sini kontrol edin
- Bot'un çalıştığından emin olun

### Yönetici Komutları Çalışmıyor
- `app/config/admin_config.py` dosyasında numaranızın doğru olduğundan emin olun
- Numara formatı: `whatsapp:+905551234567`

## Alternatif Yöntemler

### 1. Başka Ücretsiz Servisler
- **Callmebot** (daha basit)
- **WhatsApp Business API** (ücretli)
- **Meta WhatsApp API** (ücretli)

### 2. Manuel Test
Bot çalışmıyorsa, önce basit bir test yapın:
```python
# test_whatsapp.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    message = request.values.get('Body', '')
    return f"Mesaj: {message}"

app.run(port=5000)
``` 