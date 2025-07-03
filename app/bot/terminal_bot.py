from api.price_api import get_current_price

def handle_customer_message(message):
    message = message.lower()

    if "fiyat" in message:
        price_info = get_current_price()

        if price_info is None:
            return "Fiyatlar henüz açıklanmadı."
        else:
            return f"Güncel Fiyat: {price_info['price_per_kg']} {price_info['currency']}"
    else:
        return "Anlayamadım, Sadece 'fiyat' kelimesiyle sorgu yapabilirsiniz."
