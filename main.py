from app.bot.terminal_bot import handle_customer_message, get_price_and_total

def main():
    print("Hoş geldiniz!")

    while True:
        print("\nYapmak istediğiniz işlemi seçiniz:")
        print("1) Güncel demir fiyatı öğrenme")
        print("2) Belirtilen kg için toplam fiyat hesaplama")
        print("3) Çıkış")

        selection = input("Seçiminiz: ").strip()

        if selection == "1":
            response = handle_customer_message("1")
            print(response)

        elif selection == "2":
            response = handle_customer_message("2")
            print(response)
            kg = input("Kaç kg? ").strip()
            if kg.replace(".", "", 1).isdigit():
                kg = float(kg)
                result = get_price_and_total(kg)
                print(result)
            else:
                print("Geçersiz değer. Lütfen sayı girin.")

        elif selection == "3":
            print("Görüşmek üzere.")
            break

        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
