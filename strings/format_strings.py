# Biz pythondagi variable mavzusida o'rganganimizdek biz string va numberlarni quyidagicha combine qila olmaymiz.
age = 36
# bu bizga error qaytaradi
txt = "My name is John. I am " + age
print(txt)

# Lekin biz number va string larni f-strings yoki format() methodi orqali qilishimiz mumkin.
# F-String python ning 3.6 versiyasi chiqdi va hozir format stringni preferred usuli hisoblanadi
# F-String dan foydalanish uchun string ni boshiga f belgisini yo'yish va numberni curly bracket {} ga o'rash kerak
age = 36
txt = f"My name is John. I am {age}"


# Placeholders and Modifiers - to'ldiruvchilar funksiya, o'zgaruvchi va formatlash methodlari bolishi mumkin
price = 56
txt = f"The price is {price} dollars"


# Joyegallovchi (placeholder) qiymatni formatlash uchun modifikatordan foydalanishi mumkin.
#  Modifikator qoʻshish uchun ikki nuqta : va undan keyin ruxsat etilgan formatlash turi yoziladi.
#  Masalan, .2f shakli oʻnli kasrdan keyin 2 ta raqam boʻlgan qoʻzgʻalmas nuqtali sonni anglatadi.

price = 56
txt = f"The price is {price:.2f} dollars"

# Joyegallovchi (placeholder) Python kod bo'lishi ham mumkin, masalan matematik operatsiyalar
txt = f"The price is {20 * 59} dollars"
