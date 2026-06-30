print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b a dan katta")
else:
    print("b a dan katta emas")



print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# False bo'ladiganlар:

print(bool(0))    # False ← nol
print(bool(""))   # False ← bo'sh string
print(bool([]))   # False ← bo'sh list
print(bool(None)) # False ← None
# True bo'ladiganlar:

print(bool(15))      # True ← noldan boshqa har qanday son
print(bool("Hello")) # True ← bo'sh bo'lmagan string
print(bool([1,2,3])) # True ← bo'sh bo'lmagan list

# Qoida: Bo'sh yoki nol → False, qolgan hamma narsa → True

name = input("Ismingiz: ")

if name:              # isdecimal() o'rniga shunchaki tekshirish
    print("Salom " + name)
else:
    print("Ism kiritilmadi!")  # bo'sh string → False


# Pythonda boolean type qaytaradigan isinstance() methodi bor. Uni vazifasi objectni type ni tekshirish
x = 200
print(isinstance(x, int))