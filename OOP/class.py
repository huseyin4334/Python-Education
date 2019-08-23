#class yapisi ve kullanimi

#class tanımı başına class yazılarak başlanır.
class Matematik(object):
    def topla(self, sayi1, sayi2):
        return sayi1+sayi2
    
    def cikart(self, sayi1, sayi2):
        return sayi1-sayi2
    
    def carp(self, sayi1, sayi2):
        return sayi1*sayi2
    
    def bol(self, sayi1, sayi2):
        return sayi1/sayi2
    
#instance = Örnek   Yani ben bu şekilde nesnemi oluştur
#muş oldum.
matematik = Matematik()
print("Toplam : " + str(matematik.topla(12,55)))

#biz eğer self değişkenini vermeseydik hata alırdık.
#self class'ın referansına denk gelir.

print("-----------------------Örnek 2------------------------")

class Matematik2(object):
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self):
        return self.sayi1+self.sayi2
    
    def cikart(self):
        return self.sayi1-self.sayi2
    
    def carp(self):
        return self.sayi1*self.sayi2
    
    def bol(self):
        return self.sayi1/self.sayi2
"""
Yukarıda self bir nesne tutuyor demiştik. selfin sayi1 ve sayi2 
sini atadık ve bütün fonksiyon için kullanılabilir yaptık.
Globalde bir değişken varmış gibi davrandı.
Bu kendi içinde bulunan fonksiyonlar içinde geçerlidir. Direkt
fonksiyonun ismini yazarsanız gelmez. Ancak başına self yazarsanız
o nesnenin içindeki fonksiyonlara erişebilirsiniz.
"""
    
matematik2 = Matematik2(43,22)
#bu parantezleri açınca constructor çalışır.
#bu constructor pythonda __init__ bloğudur.
print("Toplam = " + str(matematik2.cikart()))

