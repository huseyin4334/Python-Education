#tuple 1 kere tanımlandığında bir daha değiştirilemeyen veri tipidir.
#Listelere benzer özelliklere sahiptir. Ancak önemli farklılıklara sahiptir.

tuplelist = (1,2,3,"Ankara",(2,3,4,"İstanbul"),[1,2,3,[3,4,5]])
liste = [2,3,4,5,"Ankara",(2,3,4,"İstanbul"),[1,2,3,[3,4,5]]]

print(type(tuplelist))
print(type(liste))

print(tuplelist)
print(liste)

print(len(tuplelist))
print(len(liste))

# tuple'lar 2 metoda sahipler.
print(tuplelist.index("Ankara"))
print(tuplelist.count("Ankara"))


# Şimdi farklılıkları görme vakti...

# liste[0] = "hüseyin"
# tuplelist[0] = 6

#Evet hata aldık. Tuple'lar read only'dir. Bu sebeple değişklik yapamazsınız. 
#Sistem değişiklik yapılmadığını bildiği için listeye göre yapılan işlemler daha az maliyetli.

print(tuplelist[-2])
print(liste[-2])

#Sağdan 2.elemanı döndürür.

print(tuplelist[1:2])
print(liste[1:2])

#(2,) ve [3] değerini aldınız. Yanına virgül konarak gösterilmesinin sebebi string olmadığını göstermek
#içindir.

tupleDeger = ("Huseyin")
tupleDeger2 = ("huseyin",)

# print(type(tupleDeger) + " -- " + tupleDeger)
# print(type(tupleDeger2) + " -- " + tupleDeger2)

# str -- Huseyin
# tuple -- (huseyin,)

# Yukarıda yazılan yorumu yukarıdaki örnekte daha iyi anlamışsınızdır.

#iki tuple'ı birleştirme.
yeniTuple = tuplelist + tupleDeger2

#listeyi tuple yapma işlemi
donusum = tuple(liste)
donusum2 = list(tuplelist)


