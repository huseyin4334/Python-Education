# Örnek 1
class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
person1 = Person("Hüseyin","Kalçık", 21)

print(person1.age)
print(person1.firstname)
print(person1.lastname)

#İnheritance Örnek 2

class Worker(Person):
    def __init__(self,maas):
        self.maas = maas

class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

#class tanımlamalarından sonra parantezleri arasına Person yazarak
# demek istediğimiz, sen Person class'ının bir çoçuğusun 
#ve artıık Person class'ının özelliklerini miras aldın.

ahmet = Worker()
ahmet.age = 23
ahmet.maas = 2500
ahmet.firstname = "Ahmet"

mehmet = Customer()
mehmet.creditCardNumber = 112233445566
mehmet.firstname = "Mehmet"
