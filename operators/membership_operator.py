# Pythonda membership operatorlar ketma-keltlikni ichida object mavjud yokida mavjud emasligini tekshirib beradi

# in - true qaytaradi qachonki shu object mavjud bolsa
# not in - true qaytaradi qachonki shu object mavjud bolmasa

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

# membership operatorlar stringlar bilan ham ishlaydi
text = "Hello world"
print("H" in text)
print("hello" in text)
print("z" not in text)

