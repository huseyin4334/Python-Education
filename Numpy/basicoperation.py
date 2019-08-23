import numpy as np

a = np.array([12,34,45,56])
b = np.arange(4)

#her elemanı kendi indisindeki değerle işleme soktu.
c = a - b
print(c)

a = np.array([12,34,45,56,34])
b = np.arange(4)

#Hata!!
c = a - b
print(c)

d = b**2
print(d)

e = 10*np.sin(a)
print(e)

print(e<7)

#işlem yine indis indis gerçekleşti.
print(a*b)  #elementwise product

# iki vektörün matris çarpımını yapan 2 yöntem aşağıdaki gibidir.
print(a@b)
print(a.dot(b))

#verilen satır sütun bülgisine göre 1'ler ve 0'lar dan oluşan vektörler oluşturalım.
f = np.ones((3,6))
g = np.zeros((2,4))
print(f)
print(g)

#0 ile 1 arasında random değer üreterek 2'ye 4'lük bir vektör oluştur.
h = np.random.random((2,4))
print(h)

#vektör değerlerini toplayan metoddur.
i = np.sum(b)
print(b)
print(i)

#Vektördeki max değer.
print(np.max(h))
#Transpoz alma yöntemi
print(h.T)

#değerlerin kare kökünü alma
l = np.sqrt(b)
print(l)

