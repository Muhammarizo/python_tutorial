# Bitwise operatorlar (bit darajasidagi operatorlar)
# Bitwise operatorlar (binar) sonlarni taqqoslash uchun ishlatiladi. Yani - sonni o'nlik holatda emas, balki bit (0 va 1) 
# ko'rinishida ko'rib, har bir bitni alohida solishtiradi.

# & - AND - ikkala bit ham 1 bo'lsa - natija 1
# | - OR - bittasi yoki ikkalasi 1 bo'lsa - natija 1
# ^ - XOR - Faqat bittasi 1 bo'lsa - natija 1
# ~ NOT - barcha bitlarni teskari qiladi
# << - Left shift - chapga siljitadi (o'ngdan nol qo'shadi)
# >> - Right shift - o'ngga siljitadi

print(6 & 3)  # 2
# 6  →  0110
# 3  →  0011
# -----------
# &  →  0010   = 2

print(6 | 3)  # 7
# 6  →  0110
# 3  →  0011
# -----------
# |  →  0111   = 7
# Bittasi yoki ikkalasi 1 bo'lsa — natija 1.


print(6 ^ 3)  # 5
# 6  →  0110
# 3  →  0011
# -----------
# ^  →  0101   = 5
# Faqat bittasi 1 bo'lsa — natija 1. (Ikkalasi ham 1 yoki ikkalasi ham 0 bo'lsa — 0)

x = 6
print(~x)  # -7
# Barcha bitlarni teskari qiladi (0 → 1, 1 → 0). Natija manfiy songa aylanadi.

x = 3
print(x << 2)  # 12
# 3       →  0011
# 3 << 2  →  1100   = 12
# Bitlarni chapga suradi, o'ngdan nollar qo'shiladi. Bu aslida 2 ga ko'paytirishga teng (har bir siljish uchun).

x = 12
print(x >> 2)  # 3
# Bitlarni o'ngga suradi. Bu 2 ga bo'lishga teng.



# Qachon ishlatiladi ? Flags (bayroqlar) bilan ishlash
READ = 1   # 001
WRITE = 2  # 010
EXEC = 4   # 100

permissions = READ | WRITE   # 011 — o'qish va yozish ruxsati

# Bitwise operatorlar asosan past darajadagi dasturlashda (xotira, fayl ruxsatlari, tarmoq protokollari) ishlatiladi. Oddiy dasturlashda kamdan-kam kerak bo'ladi.

