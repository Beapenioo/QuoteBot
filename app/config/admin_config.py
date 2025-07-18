# Yönetici konfigürasyonu
# Bu dosyayı kendi yönetici bilgilerinizle güncelleyin

# WhatsApp yönetici telefon numaraları
WHATSAPP_ADMIN_PHONES = [
    "whatsapp:+905417189074"
]

# Yönetici kontrol fonksiyonları
def is_whatsapp_admin(phone_number: str) -> bool:
    """WhatsApp kullanıcısının yönetici olup olmadığını kontrol eder"""
    return phone_number in WHATSAPP_ADMIN_PHONES 