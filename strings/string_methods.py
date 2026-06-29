# Pythonda bir nechta string ustida amal bajaradigan buil-in methodlar mavjud.
# Yodda tuting! Barcha String methodlari yangi qiymay qaytaradi. Ular haqiqiy stringni o'zgartirmaydi

# capitilize() - Bu stringni birinchi elementini katta harfga almashtiradi
name = "muhammadrizo".capitalize()
print(name)

# casefold() - stringni kichik harflarga almashtiradi. lower() bilan bir xil faqat ingliz tilida. lekin boshqa tillarda bir biridan farq qiladi
name = "muhammadrizo".casefold()
print(name)

# center() - markazlashgan string ni qaytaradi
txt = "banana" # 6ta element
x = txt.center(20, "O")
print(x)
x = txt.center(len(txt) + 14, "O") # bu yerda txt 6 ta element. demak bizda 14 element yana qo'shiladi. shunda  chap va o'n tarafga 7 tadan "O" belgisi qo'yiladi
print(x)


# count() - bu kerakli harf yoki phrase ni aynan shu stringda necha marta takrorlangaini qaytaradi
txt = "I love apples, apple are my favourite fruit"
x = txt.count("apple")
print(x)

# encode() bu stringni UTF-8 ga o'girilgan holatda qaytaradi yani binary ga.
# text.encode(encoding, errors)
# encoding — qoidasi (default: "utf-8")
# errors   — xato bo'lsa nima qilsin (default: "strict")

txt = "My Name is Muhammadrizo"
x = txt.encode()
print(x)

# errors	Optional. A String specifying the error method. Legal values are:
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	- ignores the characters that cannot be encoded
# 'namereplace'	- replaces the character with a text explaining the character
# 'strict'	- Default, raises an error on failure
# 'replace'	- replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))




# endswith() - berilgan qiymat bilan tugaganini bildiradi va true yoki false qaytaradi
# value	Required. The value to check if the string ends with. This value parameter can also be a tuple, then the method returns true if the string ends with any of the tuple values.
# start	Optional. An Integer specifying at which position to start the search
# end	Optional. An Integer specifying at which position to end the search
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# uni malum bir oraliqda tekshirish ham mumkin.
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# uni bir nechta malumot bilan tugaganini tekshirish ham mumkin. chunki nafaqat string balki tuple ham qabul qiladi
txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)




# expandtabs() - bu stringdagi tabsize larni berilgan argument baravaricha kengaytiradi. By default 8 boladi
# sintax = string.expandtabs(tabsize)
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)




# find() - bu berilgan stringni ichidan berilgan value ni qidirish uchun ishlatilinadi.
# index() bilan bir xil. Farqi index() da agar value topilmasa exception qaytaradi. Bunda esa -1 qaytaradi.
#  Syntax string.find(value, start, end)
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5,10)
print(x)

# index() bilan farqi
txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q"))





# format() metodi belgilangan qiymat(lar)ni formatlaydi va ularni stringdagi joylashuv
#  belgisiga kiritadi.format() metodi belgilangan qiymat(lar)ni formatlaydi va ularni stringdagi joylashuv belgisiga kiritadi.
# Joylashuv belgisi jingalak qavslar yordamida belgilanadi: {}.
# format() metodi formatlangan stringni qaytaradi.
txt1 = "My name is {fname}, I am {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "my name is {}, I'm {}".format("John", 36)

print(txt1)
print(txt2)
print(txt3)

# Formatting Types
# Inside the placeholders you can add a formatting type to format the result:

# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format





# format_map() - bu method dictionary dagi value larni berilgan stringga insert qiladi va formatlangan string qaytaradi
# string.format_map(dictionary)

# Parameter	    Description
# dictionary	Required. A dictionary. The values in the dictionary can be formatted and used in the string.
myvar = {"name": "Jane", "age": 36}
txt = "Happy birthday {name}, you are now on level {age}"
print(txt.format_map(myvar))







# isalnum() - bu method berilgan stringni alphanumeric ekanligiga tekshiradi yani (a-z) va (0-9) dan iboratligiga
txt1 = "Company12"
txt2 = "Company 12"
x = txt1.isalnum()
y = txt2.isalnum()
print(x)
print(y)




# isalpha() - bu method berilgan string faqat harflardan tashkil topganini tekshiradi
txt = "CompanyX"
x = txt.isalpha()
print(x)




# isascii() - bu method berilgan stringni accii belgilariga tegishli ekanini bildiradi
txt1 = "Company12312"
txt2 = "Company123фыва12"
x = txt1.isascii()
y = txt2.isascii()
print(x)
print(y)





# isdecimal() - bu berilgan stringni barcha elementlari sonlardan iborat ekanligini tekshiradi. isalpha() ga teskari
txt = "1234"
x = txt.isdecimal()
print(x)

# bu method unicode objectlar uchun ham o'rinli
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())








# isdigit() - bu ham isdecimal() bilan bir xil faqat ² belgisi bilan ham ishlaydi
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())





# isidentifier() - bu method berilgan stringni valid identifier ga teshiradi fa boolean qaytaradi.
# valid identifier deb - berilgan string faqat (a-z) va (0-9) yoki (_) lardan tashkil topganligiga aytiladi.
# Valid identifier bo'sh joydan tashil topmasligi yoki raqamlar bilan boshlanmasligi kerak
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())





# islower() - berilgan stringni barcha elementlari kichik harflardan tashkil topganini tekshiradi
# raqamlar, simvollar va bo'sh joylar tekshirilmaydi faqat alfabet harflari tekshiriladi
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())





# isnumeric() - berilgan stringni barcha elementlari numeric (0-9) bolishligiga tekshiradi.
#  ² va ¾ belgilarini ham hisobga oladi
# "-1" va "1.5" lar hisobga olinmaydi chunki unda "-" va "." belgilari bor

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())














