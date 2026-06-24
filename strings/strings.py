# qavs ichidagi qavs
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# multi-line string
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

b = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do 
eiusmod tempor incididunt ut labore et dolore magna aliqua.'''

print(a)
print(b)
# Note: multi line ishlatilganda konsolda chiqishi ham multi line bo'ladi.


# String are arrays. 
# Ko'pgina boshqa mashhur dasturlash tillarida bo'lgani kabi, Python-dagi stringlar unicode belgilarining massividir.
# Shunday bo'lsada, Pythonda belgilar tipi mavjud emas. Buning o'rniga, Python har bir belgini string sifatida ko'rib chiqadi.
# To'rtburchak qavslar string elementlariga kirish uchun ishlatilishi mumkin.
a = "Hello, World!"
print(a[1])


# Stringlar arraylar bo'lgani uchun, biz uni loop orqali aylantira olamiz. Buning uchun for loop ishlatiladi.
for x in "banana":
    print(x)


# String uzunligini aniqlash uchun len() funksiyasidan foydalaniladi.
a = "Hello, World!"
print(len(a))


# Biz String ni ichida aynan qandaydur belgi yoki phrase borligini tekshirish uchun "in" keywordidan foydalanishimiz mumkin.
txt = "The best things in life are free!"
print("free" in txt)


# if statement bilan "in" keywordidan foydalanishimiz mumkin.
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is peresent")


# Biz String ni ichida aynan qandaydur belgi yoki phrase yo'qligini tekshirish uchun "not in" keywordidan foydalanishimiz mumkin.
txt = "The best things in life are free!"
print("expensive" not in txt)


# if statement bilan "not in" keywordidan foydalanishimiz mumkin.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is Not peresent")

