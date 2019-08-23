import numpy as np

# 1 ile 10 arasına 10 dahil olacak şekilde default 50 sayı random ata.
a = np.linspace(1,10)
print(a)

# 1 ile 10 arasına 10 dahil olacak şekilde eşit aralıklarla 5 sayı ata.
a = np.linspace(1,10,5)
print(a)

# 1 ile 10 arasına 10 dahil olacak şekilde eşit aralıklarla 11 sayı ata.
a = np.linspace(1,10,11)
print(a)

# 0 ile 2pi arasında 100 adet sayı ata.
b = np.linspace(0,2*(np.pi),100)
print(b)
print(np.sin(b))