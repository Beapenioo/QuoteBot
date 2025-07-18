import os
from dotenv import load_dotenv

load_dotenv()

# .env'den yönetici numaralarını çek
admin_phones_env = os.getenv("WHATSAPP_ADMIN_PHONES", "")
WHATSAPP_ADMIN_PHONES = [num.strip() for num in admin_phones_env.split(",") if num.strip()]

def is_whatsapp_admin(phone_number: str) -> bool:
    """WhatsApp kullanıcısının yönetici olup olmadığını kontrol eder"""
    return phone_number in WHATSAPP_ADMIN_PHONES