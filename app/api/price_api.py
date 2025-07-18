def get_current_price():
    try:
        with open("app/data/price_status.txt", "r") as file:
            price = file.read().strip()
        if price == "waiting":
            return None
        return {
            "price_per_kg": float(price),
            "currency": "TRY"
        }
    except Exception as e:
        print("Hata:", e)
        return None
