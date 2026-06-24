# Stringni ichida foydalanish mumkin bo'lmagan belgilardan foydalanish uchun "escape character" dan foydalaniladi.
# Escape character backslash "\" bilan keladigan siz hohlagan belgiga aytiladi
# Illegal character foydalanishga bir misol 2 ta lik qavs ichida ishlatiladigan va 2 ta qavs orasida boladigan belgini misol qilsak boladi

# txt = "We are the so-called "Vikings" from the north"
# Bundan to'gri foydalanish uchun bizda ortiqcha ikkita ikkitalik qavs mavjud. Demak biz ikkita backslash bilan qilishimiz kerak
txt = "We are the so-called \"Vikings\" from the north"
txt = "We are the so-called \n from the north"
txt = "We are the so-called \r from the north"
txt = "We are the so-called \t from the north"
txt = "We are the so-called \b from the north"
txt = "We are the so-called \f from the north"
print(txt)

# Pythondagi boshqa escape characterlar quyidagilar:

#   \' Single Quote
#   \\ BackSlash
#   \n New Line
#   \r Carriage Return
#   \t Tab
#   \b Backspace
#   \f Form Feed
#   \ooo Octal value
#   xhh Hex value