#Identity operatorlar obyektlarni taqqoslash uchun ishlatiladi
#  — lekin ular tengligini emas, balki xuddi bir xil obyekt ekanligini, 
# bir xil xotira manzilida turganini tekshiradi.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x == y)  # True  ← qiymatlari bir xil
print(x is y)  # False ← lekin xotirada ALOHIDA obyektlar
print(x is z)  # True  ← bir xil obyekt (xotirada bitta joy)


# x  →  [xotira manzili: #100] → ["apple", "banana"]
# y  →  [xotira manzili: #200] → ["apple", "banana"]
# z  →  [xotira manzili: #100] → (x bilan bir xil!)

# x va y — ikkita alohida quticha, ichidagi narsa bir xil ko'rinsa ham.
# z esa x bilan bitta qutichaga ishora qiladi.


x = None

if x is None:      # ✅ to'g'ri usul
    print("Bo'sh")

if x == None:       # ❌ ishlaydi, lekin tavsiya etilmaydi
    print("Bo'sh")