class Mudur:
    def __init__(self,isim):
        self.isim=isim
class Okul:
    def __init__(self,okuladi,mudur):
        self.okuladi=okuladi 
        self.mudur= mudur
mudur1= Mudur("Mehmet Torunoğlu")
okul1= Okul("Kocasinan Ahmet Eren Anadolu Lisesi",mudur1)
print(okul1.mudur.isim)

