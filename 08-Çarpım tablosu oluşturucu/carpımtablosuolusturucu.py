while True:
    sayi=int(input("Lütfen çarpım tablosunu girmek istediğiniz sayıyı giriniz: "))
    for i in range(1,11):
        print(f"{sayi} *  {i} = {sayi*i}")
    while True:    
        devammi=input("Devam etmek istiyor musunuz?(E/H): ")
        if devammi=="H":
            print("Çıkış yapılıyor")
            exit()
        elif devammi=="E":
            print ("Devam ediliyor")
            break
        else:
            print("Geçersiz karakter")    
