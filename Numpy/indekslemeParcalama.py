import numpy as np

#numpy vektörleride indislerle çalışılırken pythondaki listeler gibi çalışırlar. 
sayilar = np.array([12,45,6,8,34,6,5,3,56,3,44,55,66,77,8])

print(sayilar[0])
print(sayilar[6])
#Hata!!
print(sayilar[19])

print(sayilar[0:3])
print(sayilar[::2])
print(sayilar[::-1])

sayilar2 = sayilar.reshape(3,5)
print("Çalışılan dizi : ")
print(sayilar2)

print("\n")
print("\nİndis 1 : ")
print(sayilar2[1])

print("\n1.indisin 1.indisi : ")
print(sayilar2[1][1]) #veya
print(sayilar2[1,1])

print("\ndizinin indislerinin 1.indisi : ")
print(sayilar2[:,1])

print("\ndizinin indislerinin 0.indisten 2.indise kadar olan elemanları : ")
print(sayilar2[:,0:2])

print(sayilar2[-1,:])
print(sayilar2[:,-1])

#Yukarıda kullanılan virgülün solu satırı, sağı sütunu temsil eder. İki noktada tüm anlamına gelir.