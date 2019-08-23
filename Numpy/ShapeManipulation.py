import numpy as np

#floor metodu aşağıya doğru yuvarlama yapar.
a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.shape)

# a vektörümüzü tek boyutlu bir vektör haline dönüştürür. a = a.ravel() denmediği müddetçe a'yı etkilemez.
a = a.ravel()
print(a)
print(a.reshape(2,6))

#fark ettiyseniz transpoz alınamadı. Bunun sebebi sonsuz sütun olduğu için çeviremiyor.
#Çünkü satır sabit olmak zorundadir.
print(a.T)
