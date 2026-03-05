class Telefon:
    def __init__(self,marka,fiyat,stoksayisi):
        self.marka=marka
        self.fiyat=fiyat
        self.stoksayisi=stoksayisi
    def bilgi_goster(self):   
        print(f"Marka: {self.marka} | Fiyat: {self.fiyat} | Stok sayısı: {self.stoksayisi}")    
class Magaza:
    def __init__(self,isim):
        self.telefonlar= []
        self.isim=isim
    def telefon_ekle(self,telefon):
        self.telefonlar.append(telefon)
        print("Telefon mağazaya eklendi.")    
    def bilgi_goster(self):
        if len(self.telefonlar)==0:
            print("Henüz listelenecek ürün bulunmamaktadır.")
        else:     
            print(f"Mağaza adı: {self.isim.upper()} | \nMağaza içindeki ürünler ve ürün bilgileri")
            for telefon in self.telefonlar:
                telefon.bilgi_goster()   

telefon1= Telefon("Samsung",36000,350)
telefon2= Telefon("Apple",65000,310)
magaza1= Magaza("Forum Kayseri")
magaza1.telefon_ekle(telefon1)
magaza1.bilgi_goster()
