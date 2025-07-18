# ngrok Hızlı Kurulum (5 Dakika)

## Adım 1: ngrok Hesabı Oluşturun
1. **https://dashboard.ngrok.com/signup** adresine gidin
2. **Ücretsiz hesap oluşturun** (e-posta ile)
3. **E-posta doğrulamasını** tamamlayın

## Adım 2: Auth Token Alın
1. **https://dashboard.ngrok.com/get-started/your-authtoken** adresine gidin
2. **Auth token'ınızı kopyalayın** (uzun bir metin)

## Adım 3: ngrok İndirin
1. **https://ngrok.com/download** adresine gidin
2. **Download for Windows** butonuna tıklayın
3. Zip dosyasını indirin

## Adım 4: ngrok'u Kurun
1. İndirdiğiniz zip dosyasını açın
2. `ngrok.exe` dosyasını `C:\ngrok\` klasörüne kopyalayın
3. Bu klasörü oluşturun: `mkdir C:\ngrok`

## Adım 5: Auth Token'ı Ekleyin
1. **Command Prompt** açın
2. Şu komutu çalıştırın (TOKEN_BURAYA kısmını gerçek token ile değiştirin):
```bash
C:\ngrok\ngrok.exe config add-authtoken 2zne08YFh5hvPLGLEcT044VuT80_6xYjoLdveqPHAhPFbnbH9
```

**Örnek:**
```bash
C:\ngrok\ngrok.exe config add-authtoken 2abc123def456ghi789jkl012mno345pqr678stu901vwx234yz
```

## Adım 6: ngrok'u Başlatın
```bash
C:\ngrok\ngrok.exe http 5000
```

## Adım 7: URL'yi Kopyalayın
ngrok başladığında şöyle bir çıktı göreceksiniz:
```
Forwarding    https://abc123.ngrok.io -> http://localhost:5000
```

Bu URL'yi (`https://abc123.ngrok.io`) kopyalayın.

## Adım 8: Twilio'ya Webhook URL'ini Ekleyin
1. Twilio Console'da **Messaging** > **Settings** > **Webhook**
2. **Webhook URL**'e şunu ekleyin: `https://abc123.ngrok.io/webhook`

## Test Etme
1. WhatsApp'ta Twilio sandbox numarasına mesaj gönderin
2. Bot yanıt verecektir

## Sorun Giderme

### ngrok Auth Token Hatası
```
ERROR: authentication failed: Usage of ngrok requires a verified account and authtoken.
```
**Çözüm:** Adım 1 ve 2'yi tamamlayın, sonra Adım 5'i yapın.

### ngrok Komutu Tanınmıyor
```
ngrok : The term 'ngrok' is not recognized
```
**Çözüm:** Tam yolu kullanın: `C:\ngrok\ngrok.exe`

### Bot Yanıt Vermiyor
- ngrok URL'sinin doğru olduğundan emin olun
- Twilio webhook URL'sini kontrol edin
- Bot'un çalıştığından emin olun

## Hızlı Komutlar
```bash
# Auth token ekleme
C:\ngrok\ngrok.exe config add-authtoken TOKEN_BURAYA

# ngrok başlatma
C:\ngrok\ngrok.exe http 5000

# Bot başlatma
python run_twilio_whatsapp.py
``` 