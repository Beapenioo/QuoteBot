from app.bot.price_manager import set_price

def admin_menu():
    while True:
        new_price = input("Yeni fiyat girin (çıkmak için 'q'): ")
        if new_price.lower() == 'q':
            break
        elif new_price.replace(".", "", 1).isdigit():
            set_price(new_price)
            print(f"Yeni fiyat {new_price} olarak kaydedildi.")
        else:
            print("Geçersiz değer. Lütfen sayı girin.")

if __name__ == "__main__":
    admin_menu()
