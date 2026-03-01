class Kitap:
    def __init__(self,isim,yazar,isbn):
        self.isim=isim
        self.yazar=yazar
        self.isbn=isbn
        self.odunc_durumu= False
    def bilgi_goster(self):
        durum="Ödünç verildi" if self.odunc_durumu else "Müsait"    
        print(f"Kitabın ismi: {self.isim} | Kitabın yazarı: {self.yazar} | Kitabın isbn numarası: {self.isbn} | Durumu: {durum}")
class Uye:
    def __init__(self,isim,uye_id):
        self.isim=isim
        self.uye_id=uye_id
        self.odunc_aldıgı_kitaplar=[]
    def bilgi_goster(self):
        print(f"Üyenin ismi: {self.isim} | Üyenin ID'si: {self.uye_id} | Ödünç alınan kitap sayısı: {len(self.odunc_aldıgı_kitaplar)}")    
class Kutuphane:
    def __init__(self):
        self.kitaplar=[]
        self.uyeler=[]
    def kitapekle(self,isim,yazar,isbn):
        yeni_kitap=Kitap(isim,yazar,isbn)   
        self.kitaplar.append(yeni_kitap) 
        print("Kitap kaydı başarı ile gerçekleşti")
    def uyeekle(self,isim,uye_id):
        yeni_uye=Uye(isim,uye_id)
        self.uyeler.append(yeni_uye)  
        print("Üye kaydı başarı ile gerçekleşti")
          