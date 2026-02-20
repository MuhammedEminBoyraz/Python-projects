while True:
    print("="*75)
    print("GİRİLEN SAYILARIN KARŞILAŞTIRMA OPERATÖRLERİ İLE ÇEŞİTLİ KOMBİNASYONLARI")
    print("="*75)   
    sayi1=int(input("Lütfen birinci sayıyı giriniz: "))
    sayi2=int(input("Lütfen ikinci sayıyı giriniz: "))
    print(f"{sayi1} > {sayi2} ==> {sayi1>sayi2}")
    print(f"{sayi1} < {sayi2} ==> {sayi1<sayi2}")
    print(f"{sayi1} = {sayi2} ==> {sayi1==sayi2}")
    print(f"{sayi1} eşit değildir {sayi2} ==> {sayi1!=sayi2}")
    print(f"{sayi1} >= {sayi2} ==> {sayi1>=sayi2}")
    print(f"{sayi1} <= {sayi2} ==> {sayi1<=sayi2}")
    print("="*75)
    print("GİRİLEN SAYILARIN MANTIKSAL OPERATÖRLER İLE ÇEŞİTLİ KOMBİNASYONLARI")
    print("="*75)
    print(f"{sayi1} > {sayi2} and {sayi1} > 20 ==> {sayi1 > sayi2 and sayi1 > 20}")
    print(f"{sayi1} <= {sayi2} or {sayi2} < 38 ==> {sayi1 <= sayi2 or sayi2 < 38}")
    print(f"not {sayi1} >= {sayi2} ==> {not sayi1 >= sayi2}")
    while True:
        secim=input("İşlemi tekrarlamak ister misiniz?(e/h): ")
        if secim=="e":
            print("Lütfen sayıları giriniz.")
            break
        elif secim=="h":
            print("çıkış yapılıyor...")
            exit()
        else:
            print("Geçersiz karakter girişi.")
