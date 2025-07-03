def get_current_price():
    with open("app/data/price_status.txt", "r") as file:
        price = file.read().strip()

        if price == "waiting":
            return None
        else:
            return {
                "price_per_kg": float(price),
                "currency": "TRY"
            }