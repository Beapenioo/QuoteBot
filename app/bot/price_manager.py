def set_price(new_price):
    with open("app/data/price_status.txt", "w") as file:
        file.write(str(new_price))
