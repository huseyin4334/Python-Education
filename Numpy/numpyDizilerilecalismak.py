import numpy as np

a = np.arange(1,10)
print(a)

#Bu hata verir. Sebebi bunu bir dizi değilde parametre yollamışsın gibi algılıyor.
# a = np.array(1,2,3,46,8,9,6,78,8,6,5)
# print(a)

#aşağıdaki örnekler çok önemlidir.
a = np.array([1,2,3,46,8,9,6,78,8,6,5])
print(a)
#tutulan verilerin tipini dtype ile görürüz.
print(a.dtype)

a = np.array([1.9,2,3,46,8,9,6,78,8,6,5])
print(a)
#tutulan verilerin tipini dtype ile görürüz.
print(a.dtype)

a = np.array([1.9,2,3,"46",8,9,6,78,8,6,5])
print(a)
#tutulan verilerin tipini dtype ile görürüz.
print(a.dtype)

#Şu ana kadar öğrendiklerimizin özeti
#Örnek 1
b = np.array([[1,2],[3,6],[6,9]])
print("b vektörü : "+str(b))
print("b vektörünün katman boyutu : "+str(b.ndim))
print("b vektörünün boyutu : "+str(b.shape))
print("b vektörünün tipi : "+str(b.dtype))
#Örnek 2
a = np.arange(1,10)
print("a vektörü : "+str(a))
print("a vektörünün katman boyutu : "+str(a.ndim))
print("a vektörünün boyutu : "+str(a.shape))
print("a vektörünün tipi : "+str(a.dtype))
#Örnek 3
a = a.reshape(3,3)
print("a vektörü : "+str(a))
print("a vektörünün katman boyutu : "+str(a.ndim))
print("a vektörünün boyutu : "+str(a.shape))
print("a vektörünün tipi : "+str(a.dtype))


