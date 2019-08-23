# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:34:51 2019

@author: HUSEYIN
"""

#NESNE YÖNELİMLİ PROGRAMLAMA

class VeriBilimineGiris():
    print("Basliyoruz.. Sinifima hosgeldiniz :)")
    
    adiniz = ""
    soyadiniz = ""
    baslagictarihi = 2000
    python_bilgisi = True
    bildigi_diller = []
    
def dil_ekle(veribilimci, dil):
   veribilimci.bildigi_diller.append(dil)
   return veribilimci
        
    
# GENEL YAPIYA DEGER EKLEME
VeriBilimineGiris.bildigi_diller.append("python")
VeriBilimineGiris.bildigi_diller.append("Java")
VeriBilimineGiris.bildigi_diller.append("C")
VeriBilimineGiris.bildigi_diller
# GENEL YAPIYA DEGER EKLEME

#NESNE OLUSTURMA
Ali = VeriBilimineGiris()
Ali.bildigi_diller
Ali = dil_ekle(Ali, "Java")
Ali.bildigi_diller
#NESNE OLUSTURMA

#NESNE OLUSTURMA
Veli = VeriBilimineGiris()
Veli.bildigi_diller
Veli = dil_ekle(Veli, "Kotlin")
Veli.bildigi_diller
#NESNE OLUSTURMA

#Burada büyük bir hatayı fark ediyoruz...
Ali.bildigi_diller
Veli.bildigi_diller
#Burada büyük bir hatayı fark ediyoruz...
#Yaptığımız bütün değişiklikler bütün sınıfa mal oldu.Aliye kaydettiğim
#herşey Veliyede kaydedilmiş oldu.


#ORNEK OZELLİKLER KONUSU

class VeriBilimi():
    def __init__(self):
        self.bildigidiller = []

def dil_ekle(veribilimci, dil):
   veribilimci.bildigidiller.append(dil)
   return veribilimci

#NESNE OLUSTURMA
ali = VeriBilimi()
ali.bildigidiller.append("Java")
#NESNE OLUSTURMA


#NESNE OLUSTURMA
veli = VeriBilimi()
veli.bildigidiller.append("C")
#NESNE OLUSTURMA

#cıktıları kontrol ederseniz yukardaki hatdan kurtulduğumuzu görürsünüz.
ali.bildigidiller
veli.bildigidiller

#Buradan bir çıktı alamam çünkü bu parametreyi özelleştirdik.
VeriBilimi.bildigidiller


#ORNEK OZELLİKLER KONUSU 2
class VeriBilimi():
    bildigidiller = ["Java", "R", "C"]
    def __init__(self):
        self.bildigidiller = []


#NESNE OLUSTURMA
ali = VeriBilimi()
ali.bildigidiller.append("Kotlin")
ali.bildigidiller.append("React Native")
#NESNE OLUSTURMA


#NESNE OLUSTURMA
veli = VeriBilimi()
veli.bildigidiller.append("Python")
veli.bildigidiller.append("JavaScript")
veli.bildigidiller.append("CSS")
#NESNE OLUSTURMA

#cıktıları kontrol ederseniz yukardaki hatdan kurtulduğumuzu görürsünüz.
ali.bildigidiller
veli.bildigidiller

VeriBilimi.bildigidiller





#ORNEK METHODLARI

class VeriBilimi():
    bildigidiller = ["Java", "R", "C"]
    def __init__(self):
        self.bildigidiller = []
    def dil_ekle(self, dil):
        self.bildigidiller.append(dil)

#NESNE OLUSTURMA
ali = VeriBilimi()
ali.bildigidiller.append("Kotlin")
ali.dil_ekle("React Native")
ali.dil_ekle("İOS")
#NESNE OLUSTURMA


#NESNE OLUSTURMA
veli = VeriBilimi()
veli.dil_ekle("Python")
veli.dil_ekle("JavaScript")
veli.bildigidiller.append("CSS")
#NESNE OLUSTURMA

#cıktıları kontrol ederseniz yukardaki hatdan kurtulduğumuzu görürsünüz.
ali.bildigidiller
veli.bildigidiller

VeriBilimi.bildigidiller






















