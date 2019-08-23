import numpy as np

# numpy kütüphanesini import ettik.
# bizim dizilerimizi liste denir. Numpy de buna vektör denir.
# büyük matematiksel işlemleri daha hızlı gerçekleştirir. Gruplandırmak istediğimiz verileri gruplar.

#Örneğin elinizde bir hava durumu bilgisi var.
# marmara bölgesinde istanbul 13, bursa 24 derece 
# iç anadolu bölgesinde ankara 53, konya 74 derece 
#biz bunu biliyor olabiliriz ancak bundan daha büyük veriler elimize geldiğinde bunların gruplandırılmış olması 
#önemli bir ayrıntıdır.

liste = [13,24,53,74,15,36,27,18,29,34,56,8,78]

#şimdi bunu numpy ile çalıştıralım.
#science py tarafından üretilmiştir.

#15 elemanlı(0'dan 15'e kadar) bir dizi ürettik.
a = np.arange(15)
print(a)
print(type(a))

a = a.reshape(3,5)
print(a)

#böyle bir kullanımda hata alırsınız.
#Çünkü veri kaybı veya fazlası veremezsiniz.
a = a.reshape(4,5)
print(a)
a = a.reshape(4,3)
print(a)


b = np.arange(10)
print(b)

#shape dizinin boyutunu verir. b'nin boyutu (10,) gelir. Bu 10 satırlı sınırsız sütunlu demektir.
print(b.shape)

#ndim ile boyut sayısını alırız.
print(b.ndim)
print(a.ndim)
