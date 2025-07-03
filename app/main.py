from bot.terminal_bot import handle_customer_message
from bot.price_manager import  set_price

def main():
   while True:
    user_type=input("Kullanıcı tipi (musteri/yonetici/exit): ").lower()
    
    if user_type =="musteri":
       message=input("Mesaj: ")
       response = handle_customer_message(message)
       print("Bot:",response) 

    elif user_type == "yonetici":
       price=input("Yeni fiyatı girin:")
       set_price(price)
       print("Fiyat güncellendi:",price)

    elif user_type == "exit":
       break
    
    else:
       print ("Geçersiz kullanıcı tipi. Lütfen 'musteri', 'yonetici' veya 'exit' girin.")

if __name__ == "__main__":
    main()