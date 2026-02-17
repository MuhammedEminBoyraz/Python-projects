while True:
    try:
        sayial1=int(input("Lütfen bir sayı giriniz: "))
        sayial2=int(input("Lütfen bir sayı giriniz: "))
        islem=(sayial1/sayial2)
        print(islem)
    except ValueError:
        print("YALNIZCA RAKAMLAR KULLANILABİLİR.")
        continue
    except ZeroDivisionError:
        print("PAYDA SIFIR OLAMAZ.")
        continue
    except Exception as e:
        print(f"Hata:{e}")
        continue
    sor=input("İşlemi tekrarlamak istiyuor musunuz?(E/H): ")
    if sor == "E":
        print("İşleme devam ediliyor")
        continue
    elif sor=="H":
        print("Hoşçakal") 
        break  
print("Birdaha ki sefere görüşmek üzere")         