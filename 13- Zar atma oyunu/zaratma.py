import random
while True:
    print("Birinci oyuncu için zar atılıyor...")
    birincizar=random.randint(1,6)
    print("İkinci oyuncu için zar atılıyor...")
    ikincizar=random.randint(1,6)
    if birincizar>ikincizar:
        print(f"Birinci oyuncunun attığı zar:{birincizar}, ikinci oyuncunun attığı zar:{ikincizar} | Kazanan==>BİRİNCİ OYUNCU\nTEBRİKLER")
       
    elif birincizar==ikincizar:   
        print(f"Birinci oyuncunun attığı zar:{birincizar}, ikinci oyuncunun attığı zar:{ikincizar} | BERABERE") 
        
    else:
        print(f"Birinci oyuncunun attığı zar:{birincizar}, ikinci oyuncunun attığı zar:{ikincizar} | Kazanan==>İKİNCİ OYUNCU\nTEBRİKLER")    
    while True:    
        devammi=input("Devam etmek istiyor musunuz?(E/H)").upper()
        if devammi=="E":
            print("DEVAM EDİLİYOR...")
            break
        elif devammi=="H":
            print("ÇIKIŞ YAPILIYOR") 
            break
        else: 
            print("Geçersiz giriş.Lütfen E veya H girin.")   
    if devammi=="H":
        break        