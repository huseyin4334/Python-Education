#input kullanıcıdan değer almaya yarayan fonksiyondur.
ad = input("Adınız : ")
print(ad)

#input fonksiyonu alınan değeri direkt olarak string atar.
sayi1 = input("Sayi1 : ")
sayi2 = input("Sayi2 : ")

print(sayi1 + sayi2)

# Değerleri string gibi birleştirdi. Bu sorundan kurtulmak için
#broadcasting denilen yöntemi kullanırız.

print(int(sayi1) + int(sayi2))

sayi3 = int(input("Sayi3"))
