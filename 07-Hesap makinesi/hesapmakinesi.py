def topla(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

while True:
    print("1.Toplama işlemi")
    print("2.Çıkarma işlemi")
    print("3.Çarpma işlemi")
    print("4.Bölme işlemi")
    print("0.Çıkış")
    secim=input("Lütfen yapmak istediğiniz işlem numarasını giriniz: ")
    
    if secim=="0":
        print("ÇIKIŞ YAPILIYOR")
        break  
    elif secim in ["1","2","3","4"]:
        sayi1=int(input("Lütfen birinci sayıyı giriniz: "))
        sayi2=int(input("Lütfen ikinci sayıyı giriniz: "))    
        if secim=="1":
            toplam=topla(sayi1,sayi2)
            print(toplam)
        elif secim=="2":
            fark=cikarma(sayi1,sayi2)
            print(fark)
        elif secim=="3":
            carpim=carpma(sayi1,sayi2)
            print(carpim)  
        elif secim=="4":
            if sayi2==0:
                print("Sıfıra bölme yapılamaz.")
            else:    
                bolum=bolme(sayi1,sayi2)
                print(bolum)  
    else:
        print("Geçersiz giriş.Lütfen menüdeki işlem numaralarından birini tuşlayınız")         
