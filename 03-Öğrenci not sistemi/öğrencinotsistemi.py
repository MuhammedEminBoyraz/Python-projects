ogrenciler=[]
while True:
    print("\n"+"="*40)
    print("ÖĞRENCİ NOT SİSTEMİ")
    print("="*40)
    print("1.Öğrenci ekle")
    print("2.Tüm öğrencileri listele")
    print("3.En başarılı öğrenci")
    print("0.Çıkış")
    secim=input("\nSeçim: ")
    if secim== "1":
        print("Öğrenci ekleme...")
        ad= input("Adınızı giriniz: ")
        notlar=[]
        for i in range(3):
            notdegeri=float(input(f"{i+1}. not değerinizi giriniz: "))
            notlar.append(notdegeri)
        ortalama= sum(notlar)/len(notlar)
        if ortalama>=85:
            harf="AA" 
        elif ortalama>=70:
            harf="AB"
        elif ortalama>=60:
            harf="BB"
        elif ortalama>=50:
            harf="CB"
        else: 
            harf="FF"   
        ogrenci={
            "ad":ad,
            "notlar":notlar,
            "ortalama":ortalama,
            "harf":harf
        } 
        ogrenciler.append(ogrenci)
        print("Öğrenci eklendi.")           
    elif secim=="2":
        print("Öğrenci listeleme...")
        if len(ogrenciler)==0:
            print("HENÜZ LİSTELENECEK ÖĞRENCİ YOK")
        else:    
            print("="*60)
            print("Öğrenci Listesi")
            print("="*60)
            for i in ogrenciler:
                print(i)
    elif secim=="3":
        print("En başarılı...")
        if len(ogrenciler)==0:
            print("HENÜZ LİSTELENECEK ÖĞRENCİ YOK")
        else:
            enyuksek=ogrenciler[0]
            for i in ogrenciler:
                if i["ortalama"]>enyuksek["ortalama"]:
                    enyuksek=i  
            print("\n En başarılı öğrenci:")
            print(f"Ad: {enyuksek['ad']}")  
            print(f"Ortalama: {enyuksek['ortalama']}") 
            print(f"Harf notu: {enyuksek['harf']}")           
    elif secim=="0":
        print("ÇIKIŞ")
        break
    else:
        print("Geçersiz seçim") 

           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           