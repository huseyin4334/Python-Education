message = "Merhaba Dünya"

#--------------SUBSTRİNG-----------------------------
#Bir metni parçalamak için substring kullanırız.

#2iindisteki değeri yazdir
print(message[2])

#2.indekten 7.indekse kadar(2 dahil 7 dahil değil)
print(message[2:7])

#2.indisten sona kadar yazidir
print(message[2:])

#Baştan 2.indise kadar yazidir
print(message[:2])

#diziyi tam tersinden bastırmaya yarar
print(message[::-1])

#diziyi tam tersinden 3'er karakter atlayarak bastırmaya yarar
print(message[::-3])

#diziyi 2'şer karakter atlayarak bastırmaya yarar
print(message[::2])

#dizinin son elemanını verir
print(message[-1])


"""
Sonuç olarak alınan 3 parametre var;
    Başlangıç konumu
    Bitiş konumu
    Atlanacak karakter sayısı
"""

#--------------------LEN-------------------------
# bir metnin yada dizinin boyutunu verir.
#Saymaya 0'dan başlamaz.
print(len(message))

#-------------LOWER - UPPER-------------------------
#Lower : Karakter Küçültme
#Upper : Karakter Büyütme
print(message.upper())
print(message.lower())
print(message[2::2].upper())
print(message[2::1].lower())

#------------------------REPLACE----------------------
"""
Önceden tanımlanmış metindeki karakter değişiklikleri
yapmak için kullandığımız fonksiyon replace fonksiyonudur.
Değeri kokünden değiştirmek için atama yapmak zorundayız.
"""
print(message.replace("ü","u"))
message = message.replace("ü","u")


#------------------------SPLİT - STRİP----------------------

knowledge = "    Hüseyin Kalçık 33 Kütahya    "
print(knowledge.split(" "))

knowledge = "    Hüseyin Kalçık 33 Kütahya    ".strip()
print(knowledge.split(" "))

knowledge = "    Hüseyin Kalçık 33     Kütahya    ".strip()
print(knowledge.split(" "))

knowledge = "    Hüseyin Kalçık 33 Kütahya    "
print(knowledge.split())

knowledge = "Hüseyin;Kalçık;33;Kütahya"
print(knowledge.split(";"))
print(knowledge.split(";")[2])

"""
split fonksiyonu verilen değere göre metni parçalamaya yarar.
split default çalıştığında .strip() fonksiyonunuda çalıştırır.

.strip() fonksiyonu sadece baş ve son için boşlukları temizler.

Ayracımı değiştirebilirim. Değiştirdiğim ayracıda splite parametre
olarak gönderirim
"""



