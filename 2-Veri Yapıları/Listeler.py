ogrenciler = [12 ,["hüseyin","3.sınıf"], ["engin" , "2.sınıf"], ["salih" , "1.sınıf"]]

ogrenciler.append(["ahmet", "4.sınıf"])

print(ogrenciler[2])
print(ogrenciler[2][1])
print(ogrenciler)
print(len(ogrenciler))
print(type(ogrenciler))

"""
listeler tüm veri tiplerini içlerinde barındırabilirler.
indisleri vardır ve indisler aracılığıyla verilere ulaşılır.
"""

# ----------------------LİSTE FONKSİYONLARI------------------------
sehirler = list(("İstenbul", "Ankara"))

#Listenin sonuna değer ekleme
sehirler.append("Bolu")
print(sehirler)

#clear fonksiyonu dizinin tüm elemanlarını temizler.
#En büyük özelliği print içine görmek için bile yazsanız 
#sehirler listesi tamamen boşaltılacaktır.

# print(sehirler.clear())
# print(sehirler)

#Verilen değerin dizide kaç defa geçtiğini integer değer olarak döndürür.
print(sehirler.count("Ankara"))

#Verilen değerin dizide hangi indexte olduğunu integer değer olarak döndürür.
#Daha fazla varsa ilk bulduğunun index'ini döndürür.
print(sehirler.index("Ankara"))

#Verilen değeri bulup siler.
print(sehirler.remove("Ankara"))

#Verilen indexi bulup siler.
print(sehirler.pop(1))

#İki parametre alır. İlk parametre index, ikinci parametre eklenecek değerdir.
print(sehirler.index(1,"Balıkesir"))

#Diziyi ters döndürür.
print(sehirler.reverse())

#yapılan tüm bu işlemler direkt olarak dizinin üzerinde işlem yaparlar.

"""
Listeler referans tiplerdir.
Yani adres bildirirler.
Bir diziyi başka bir parametreye atadım. Sonra 2. dizide bir değişiklik
yaptığımda iki dizi içinde bu değişiklik uygulanır. Bu durumdan kurtulmak 
için copy() fonksiyonu kullanılır. Bu fonksiyon sayesinde adresler ayrılmış olur.
"""
"""
Bu durumdan kurtulmanın bir diğer yoluda .extend() fonksiyonunu kullanmaktır.
"""
sehirler2 = sehirler
sehirler3 = sehirler.copy()
sehirler.extend(sehirler3)

sehirler2.append("İzmir")

print(sehirler)
print(sehirler2)
print(sehirler3)

# sayılar varsa küçükten büyüğe
#string ifadeler varsada A'dan Z'ye 
#sıralama yapar.
print(sehirler.sort())
