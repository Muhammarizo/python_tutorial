# Pythonda stringlar ustida amal bajarish uchun bir nechta built-in metodlar mavjud.

# Upper Case
a = "Hello, World!"
print(a.upper())


# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace - bu stringning boshidagi va oxiridagi bo'shliqni olib tashlaydi.
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String - bu stringdagi ma'lum bir so'zni boshqa so'z bilan almashtiradi. agar harf yoq bo'lsa, hech narsa qilmaydi.
a = "Hello, World!"
print(a.replace("H", "J"))


# Split String - bu stringni belgilangan separator bo'yicha bo'lib, natijada list qaytaradi.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
