def set_price(new_price):
    """
    Verilen yeni fiyatı app/data/price_status.txt dosyasına kaydeder.
    """
    with open("app/data/price_status.txt", "w", encoding="utf-8") as f:
        f.write(str(new_price)) 