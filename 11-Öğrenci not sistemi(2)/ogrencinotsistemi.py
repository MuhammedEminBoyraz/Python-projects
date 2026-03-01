ogrenciler = []
notlar = []

while True:
    print("\n" + "="*40)
    print("ÖĞRENCİ NOT SİSTEMİ")
    print("="*40)
    print("1. Öğrenci ekle")
    print("2. Tüm öğrencileri listele")
    print("3. Öğrenci ara")
    print("4. En yüksek ortalamayı bul")
    print("5. Genel ortalama hesapla")
    print("0. Çıkış")
    
    secim = input("\nSeçiminiz: ")
    
    if secim == "1":
        isim = input("Öğrenci adı: ")
        ogrenci_notlari = []
    
        while len(ogrenci_notlari) < 3:  # ← 3 not toplayana kadar
            try:
                not_degeri = int(input(f"{len(ogrenci_notlari)+1}. not: "))
                
                if 0 <= not_degeri <= 100:
                    ogrenci_notlari.append(not_degeri)
                else:
                    print("Not 0-100 arası olmalı!")
                    
            except ValueError:
                print("Lütfen sayı girin!")
            
        ogrenciler.append(isim)
        notlar.append(ogrenci_notlari)
        print("✓ Öğrenci eklendi!")
        
    elif secim == "2":
        if len(ogrenciler) == 0:
            print("Henüz öğrenci yok!")
        else:
            print("\n" + "="*50)
            for i in range(len(ogrenciler)):
                print(f"İsim: {ogrenciler[i]} | Notlar: {notlar[i]}")
            print("="*50)
            
    elif secim == "3":
        aranan_isim = input("Aranacak isim: ")
        aranan_isim = aranan_isim.lower()  # ← Düzeltildi
        bulundu = False
        
        for i in range(len(ogrenciler)):
            if ogrenciler[i].lower() == aranan_isim:  # ← Düzeltildi
                print(f"✓ Bulundu! İsim: {ogrenciler[i]} | Notlar: {notlar[i]}")
                bulundu = True
                
        if not bulundu:
            print("Öğrenci bulunamadı!")
            
    elif secim == "4":
        if len(ogrenciler) == 0:
            print("Henüz öğrenci yok!")
        else:
            en_yuksek = 0
            en_yuksek_isimler = []
            
            for i in range(len(ogrenciler)):
                ortalama = sum(notlar[i]) / len(notlar[i])
                
                if ortalama > en_yuksek:
                    en_yuksek = ortalama
                    en_yuksek_isimler = [ogrenciler[i]]  # ← Düzeltildi
                elif ortalama == en_yuksek:
                    en_yuksek_isimler.append(ogrenciler[i])
                    
            print(f"\n En yüksek ortalama: {en_yuksek:.2f}")
            print(f"Öğrenciler: {', '.join(en_yuksek_isimler)}")
            
    elif secim == "5":
        if len(ogrenciler) == 0:
            print("Henüz öğrenci yok!")
        else:
            toplam_not = 0
            toplam_not_sayisi = 0
            
            for i in range(len(ogrenciler)):
                toplam_not += sum(notlar[i])
                toplam_not_sayisi += len(notlar[i])
                
            genel_ortalama = toplam_not / toplam_not_sayisi
            print(f"\n Genel ortalama: {genel_ortalama:.2f}")
            
    elif secim == "0":
        print("Çıkış yapılıyor... Hoşça kalın!")
        break
        
    else:
        print("Geçersiz seçim! Lütfen 0-5 arası seçim yapın.")
    


