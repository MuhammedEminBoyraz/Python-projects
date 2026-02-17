class bankahesabi:
    def __init__(self,isim):
        self.isim=isim
        self.bakiye=0
    def parayatir(self,miktary):
         self.bakiye=(self.bakiye+miktary)
         print(f"Güncel hesap bakiyeniz:{self.bakiye}") 
    def paracek(self,miktarc):
        if self.bakiye>=miktarc:
            self.bakiye=(self.bakiye-miktarc)
            print(f"Güncel hesap bakiyeniz:{self.bakiye}")
        else:
            print("Hesap bakiyeniz yetersiz!")    
    def bakiyegösterme(self):
        print(f"Güncel hesap bakiyeniz:{self.bakiye}")

ahmet=bankahesabi("Ahmet")
ahmet.bakiyegösterme()
ahmet.parayatir(28000)
ahmet.paracek(7500)
