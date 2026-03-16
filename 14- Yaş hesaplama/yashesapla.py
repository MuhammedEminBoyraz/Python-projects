from datetime import date

while True:
    print("\n--- YAŞ HESAPLAMA ---")
    print("1. Hangi yılda olduğumuzu söyle")
    print("2. Kaç yaşında olduğumu söyle")
    print("3. 100 yaşına kaç yıl kaldığını söyle")
    print("4. Hangi yılda 100 yaşında olduğumu söyle")
    
    secim = input("\nİşlem numarası: ")
    bugun = date.today().year
    
    if secim == "1":
        print(f"Şu anda {bugun} yılındayız.")
    
    elif secim in ["2", "3", "4"]:
        dogumyili = int(input("Doğum yılınızı giriniz: "))
        yas = bugun - dogumyili
        
        if secim == "2":
            print(f"Şu anda {yas} yaşındasınız")
        elif secim == "3":
            print(f"100 yaşına kalan süre: {100 - yas} yıl")
        elif secim == "4":
            print(f"{dogumyili + 100} yılında 100 yaşında olacaksınız!")
    
    else:
        print("Geçersiz seçim!")
    
    # Devam kontrolü
    while True:
        devammi = input("\nDevam etmek istiyor musunuz? (e/h): ").lower()
        if devammi == "e":
            print("Devam ediliyor...")
            break
        elif devammi == "h":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen e veya h giriniz.")
    
    if devammi == "h":
        break





