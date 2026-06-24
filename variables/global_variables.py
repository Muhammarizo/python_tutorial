# Global variables deb funksiyadan tashqarida elon qilingan barcha o'zgaruvchilarga aytiladi.
#  Global o'zgaruvchilarni har qanday funksiya ichida ishlatish mumkin

x = "awasome"

def myfunc():
    print("Python is " + x)

myfunc()


# agar global o'zgaruvchini nomi funksiya ichidagi o'zgaruvchi bilan bir xil bo'lsa, bu local variable ga aylanadi.

a = "awasome"

def myfunc():
    a = "fantastic"
    print("Python is " + a)

myfunc()

print("Python is " + a)

# endi shu yerda savol tug'iladi, agar global o'zgaruvchini funksiya ichida ishlatmoqchi bo'lsak, qanday qilib qilamiz?
# buning uchun global kalit so'zidan foydalanamiz.

def myfunc():
    global a # bu yerda global kalit so'zi a o'zgaruvchisini global deb belgilaydi va endi u global o'zgaruvchi sifatida ishlatiladi va alohida qatorda yozilishi kerak. global a = "fantastic" bu xato bo'ladi, chunki global kalit so'zi faqat o'zgaruvchini global deb belgilaydi va unga qiymat berish uchun alohida qatorda yozilishi kerak.
    a = "fantastic"
    print("Python is " + a)