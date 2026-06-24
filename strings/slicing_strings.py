# Stringlarni kesish (slicing) usuli Python dasturlash tilida matnlarni kesish va ulardan ma'lumot olish uchun ishlatiladi.
# Buning uchun boshlang'ich va tugash indekslarini belgilash kerak. Kesish usuli quyidagi sintaksisga ega:
# string[start:end]
b = "Hello, World!"
print(b[2:5])  
# Natija: llo. Bundan ko'rinadiki, kesish usuli 2-indeksdan boshlanadi va 5-indeksgacha bo'lgan belgilarni oladi, lekin 5-indeksdagi belgi olinmaydi.


# Agar biz boshlang'ich indeksni belgilamasak, kesish usuli 0-indeksdan boshlanadi.
b = "Hello, World!"
print(b[:5])
# Natija: Hello. Bu yerda kesish usuli 0-indeksdan boshlanadi va 5-indeksgacha bo'lgan belgilarni oladi, lekin 5-indeksdagi belgi olinmaydi.


# Agar biz tugash indeksini belgilamasak, kesish usuli oxirgi indeksgacha bo'lgan belgilarni oladi.
b = "Hello, World!"
print(b[2:])
print(b[2:len(b)])
# Natija: llo, World!. Bu yerda kesish usuli 2-indeksdan boshlanadi va oxirgi indeksgacha bo'lgan belgilarni oladi.



# Negative indekslar ishlatilganda, kesish usuli oxirgi belgidan boshlab hisoblanadi.
# Yani bu holatda -5 ohirida orqaga sanab kelingadagi W belgisi boladi lekin teskari ishlagani uchun endi bu holatda W belgisi tashlab yuboriladi
# va -2 ohirida orqaga sanab kelingadagi r belgisi boladi lekin teskari ishlagani uchun endi bu holatda r belgisi tashlab yuborilmaydi
b = "Hello, World!"
print(b[-5:-2])



