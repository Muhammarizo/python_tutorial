# pythonda quyidagi ma'lumot turlari mavjud:

# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType



# Biz har qanday o'zgaruvchini data type ni bilishimiz mumkin, buni type() funksiyasi yordamida qilamiz.
x = 5
print(type(x))



# Pythonda data type o'zgaruvchiga qiymat berilganda avtomatik ravishda aniqlanadi.
#  Buni dynamic typing deyiladi. Masalan, x o'zgaruvchiga 5 qiymati berilgan va u int data type ga ega bo'ladi, 
# keyin esa x o'zgaruvchiga "Hello World" qiymati berilgan va u str data type ga ega bo'ladi.
x = "Hello World"     # data type str
x = 20                 # data type int
x = 20.5               # data type float
x = 1j                 # data type complex
x = ["apple", "banana", "cherry"] # data type list
x = ("apple", "banana", "cherry") # data type tuple
x = range(6)             # data type range
x = {"name": "John", "age": 36}   # data type dict
x = {"apple", "banana", "cherry"} # data type set
x = frozenset({"apple", "banana", "cherry"}) # data type frozenset
x = True                 # data type bool
x = b"Hello"            # data type bytes
x = bytearray(5)         # data type bytearray
x = memoryview(bytes(5)) # data type memoryview
x = None                 # data type NoneType



# agar specific data type ga ega bo'lishni xohlasak, biz o'zgaruvchiga qiymat berishda data type ni ko'rsatishimiz mumkin.
#  Buni casting deyiladi. Masalan, x o'zgaruvchiga 5 qiymati berilgan va u int data type ga ega bo'ladi, 
# keyin esa x o'zgaruvchiga "Hello World" qiymati berilgan va u str data type ga ega bo'ladi.
x = str("Hello World") # data type str
x = int(20)            # data type int
x = float(20.5)        # data type float
x = complex(1j)        # data type complex
x = list(("apple", "banana", "cherry")) # data type list
x = tuple(("apple", "banana", "cherry")) # data type tuple
x = range(6)             # data type range
x = dict(name="John", age=36)   # data type dict
x = set(("apple", "banana", "cherry")) # data type set
x = frozenset(("apple", "banana", "cherry")) # data type frozenset
x = bool(5)                 # data type bool
x = bytes(5)            # data type bytes
x = bytearray(5)         # data type bytearray
x = memoryview(bytes(5)) # data type memoryview
