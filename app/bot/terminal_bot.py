from app.api.price_api import get_current_price

def get_price_and_total(kg):
    price_info = get_current_price()
    if price_info:
        total_price = price_info["price_per_kg"] * kg
        return f"{kg} kg demir için toplam fiyat: {total_price:.2f} {price_info['currency']}"
    else:
        return "Fiyatlar henüz açıklanmadı."

def handle_customer_message(message):
    if message == "1":
        price_info = get_current_price()
        if price_info:
            return f"Güncel demir fiyatı: {price_info['price_per_kg']} {price_info['currency']}"
        else:
            return "Fiyatlar henüz açıklanmadı."
    elif message == "2":
        return "Kaç kg demir için fiyat hesaplayalım?"
    else:
        return "Geçersiz seçim. Lütfen '1' ya da '2' yazınız."
