#setler index'siz ve sırasız elemanlardan oluşur.
#Veri tekrarı söz konusu değildir. Tüm elemanları eşsizdir. Yani bir tuple'ın içinde "huseyin"
# stringi varsa bir tane daha alamaz.
# {} ile tanımlanır.
#setler de read only'dir. İçinde bulunan değerlere müdahale edemiyoruz. Ancak ekleme ve update yapabiliyoruz.
#oldukça hızlı çalışırlar.
#Genel fonksiyonları kullanabiliyoruz. (len, dir, type vb)


veriseti = {"engin", "derin", "salih", "hüseyin"}

print(veriseti)

for isimler in veriseti:
    print(isimler)
    
# in keyword'ü bizim verdiğimiz dizi,tuple vb veri tutan birimlerde kontrol işlemi yapmayı sağlar.
print("derin" in veriseti)

if "derin" in veriseti:
    print("Evet içinde var.") 
else:
    print("İçinde Yok")


veriseti.add("kamil")
print(veriseti)

veriseti.update(["semih", "kaan", "yalcin"])
print(veriseti)

#eleman silme fonksiyonu eğer o elemanı bulamazsa hata alırız.
veriseti.remove("semih")
print(len(veriseti))

#eleman silerken o elemanı bulamazsa hata alıyorduk ama ben hata görmek istemiyorum. Arıza çıkarmadan 
#yoluna devam etsin istiyorum. O zaman discard metodunu kullanmalıyım.
veriseti.discard("selin")
print(len(veriseti))

#ben isim vermeden bir eleman silmek istiyorum diyorsan pop fonksiyonunu kullanıyoruz.
#sondan diyemiyorum çünkü sette index yoktu.
veriseti.pop()
print(len(veriseti))

#setin içini tamamen silme işlemi
veriseti.clear()

#seti tamamen yok eder.
del veriseti

student = set([",","a","ww","aa"])
#bu şekilde de bir tanımlama yapabiliriz.


#-------------------------------------UNION KEYWORD--------------------------------------------
#sıralı birşekilde iki listenin elemanlarını tekrarsız şekilde olacak şekilde birleştirir.

setA = {1,2,3,4,5,6}
setB = {1,2,3,7,8,9,0}

print(setA | setB)
print(setA.union(setB))
print(setA)
print(setB)



