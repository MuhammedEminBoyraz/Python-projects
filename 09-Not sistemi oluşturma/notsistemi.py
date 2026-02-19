'''Not Harf Dönüştürücü!
Kullanıcıdan 0-100 arası not alın ve harf notuna çevirin.
Harf Notu Sistemi:

90-100 → AA
80-89 → BA
70-79 → BB
60-69 → CB
50-59 → CC
40-49 → DC
30-39 → DD
0-29 → FF

Ekstra:

0-100 dışı → Hata
Tekrar sorsun'''

notdegeri=int(input("Lütfen almış olduğunuz notu giriniz: "))
if notdegeri>=90 and 100>=notdegeri:
     print("Harf notu: AA")
elif 90>notdegeri and notdegeri>=80:
    print("Harf notu: BA")
elif 80>notdegeri and notdegeri>=70:
    print("Harf notu: BB")
elif 70>notdegeri and notdegeri>=60:
    print("Harf notu: CB")
elif 60>notdegeri and notdegeri>=50:
    print("Harf notu: CC")  
elif 50>notdegeri and notdegeri>=40:
    print("Harf notu: DC")
elif 40>notdegeri and notdegeri>=30:
    print("Harf notu: DD")
elif 30>notdegeri and notdegeri>=0:
    print("ED")
else:
    print("Geçersiz not değeri. Lütfen 0-100 arası bir değer giriniz.")                       


