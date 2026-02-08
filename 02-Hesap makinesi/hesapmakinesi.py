x=1
while x==1:
    try:     
        sayi1= int(input("Bir sayı giriniz: "))
        islemsec=input("Yapmak istediğiniz işlemi giriniz: ")
        sayi2= int (input("Bir sayı giriniz: "))  
    except ValueError:
        print("Yalnızca rakam girebilirsiniz.")          
    if islemsec=="+":
        print("İşleminizin sonucu: "+str(sayi1+sayi2))
    elif islemsec=="-":
        print("İşleminizin sonucu: "+str(sayi1 - sayi2))
    elif islemsec=="*":
        print("İşleminizin sonucu: "+str(sayi1*sayi2))
    elif islemsec=="/":
        if sayi2==0:
            print("Sıfır ile bölme yapılamaz.")
        else:    
            print("İşleminizin sonucu: "+str(sayi1/sayi2))
        
    else:
        print("Lütfen dört işlemden birini seçiniz: (+,-,*,/)")
    devammi= input("Devam etmek istiyor musunuz?(EVET/HAYIR): ")
    if devammi=="EVET":
        continue
    else:
        break
    