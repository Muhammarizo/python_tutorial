# Pythonda 3 ta asosiy numeric data type lar mavjud:

# int, 
# float 
# complex.

# Misollar:
x = 5           # int
y = 3.14        # float
z = 1j          # complex

# Int yoki integer butun son bo'lib, u musbat yoki manfiy bo'lishi mumkin va cheksiz uzunlikka ega.
x = 1
y = 35656222554887711
z = -3255522

# Float yoki "floating point number" - bu musbat yoki manfiy bo'lgan, bitta yoki bir nechta o'nlik raqamlarni o'z ichiga olgan son.
x = 1.10
y = 1.0
z = -35.59

#  Float "e" belgisi bilan ishlatilib, ilmiy sonlar bilan ham ishlatilishi mumkin yani 10 darajasi degan manoda. 
x = 35e3
y = 12E4
z = -87.7e100



# Complex sonlar "j" yoki "J" bilan ishlatiladi. Complex sonlar real va tasavvuriy qismlardan iborat bo'lib, 
# ular quyidagi shaklda ifodalanadi: a + bj, bu yerda a real qism va b tasavvuriy qismdir.
x = 3+5j
y = 5j
z = -5j


# Type conversion yoki typecasting - bu bir data type ni boshqa data type ga o'zgartirish jarayonidir.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
# Biz complex sonlarni boshqa data type ga o'zgartira olmaymiz!.


# Random number generator - bu tasodifiy sonlarni yaratish uchun ishlatiladigan moduldir.
# Python da random sonlarni yaratadigan method yo'q, lekin random modulidan foydalanib, random sonlarni yaratishimiz mumkin.
import random
print(random.randrange(1,10))





