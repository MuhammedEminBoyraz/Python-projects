while True:
    print("1-Yeni giriş yaz\n")
    print("2-Tüm girişleri oku\n")
    print("0-Çıkış\n") 
    
    secim=input("Seçiminiz: ")
    
    if secim=="1":
        print("Yazmaya başlayabilirsiniz\n")
        
        with open("günlük.txt","a",encoding="utf-8") as dosya:
            icerik=input()
            dosya.write(icerik+"\n")
    elif secim=="2":
        try:
            with open("günlük.txt", "r", encoding="utf-8") as dosya:
                metin = dosya.read()
                print(metin)
        except FileNotFoundError:   
            print("İçerik bulunamadı")
    elif secim=="0":
        print("Çıkış yapılıyor")
        break
    else:
        print("Geçersiz seçim")
                    

