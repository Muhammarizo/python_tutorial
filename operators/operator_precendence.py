# Operator Precedence (Operatorlar ustuvorligi)
# Operator precedence — bu amallar qaysi tartibda bajarilishini ko'rsatadi.


print(100 + 5 * 3)  # 115, 315 emas!
# Chunki ko'paytirish (*) qo'shishdan (+) ustun — avval 5*3=15 hisoblanadi, keyin 100+15=115.


# Python Operator Precedence (yuqoridan pastga, kuchlidan kuchsizga)

# 1.  ()                                          - Qavslar
# 2.  **                                           - Darajaga ko'tarish
# 3.  +x  -x  ~x                                   - Unar plus/minus, bitwise NOT
# 4.  *  /  //  %                                  - Ko'paytirish, bo'lish, butun bo'lish, qoldiq
# 5.  +  -                                         - Qo'shish, ayirish
# 6.  <<  >>                                       - Bitwise chap/o'ng siljitish
# 7.  &                                            - Bitwise AND
# 8.  ^                                            - Bitwise XOR
# 9.  |                                            - Bitwise OR
# 10. ==  !=  >  >=  <  <=  is  is not  in  not in - Taqqoslash, identity, membership
# 11. not                                          - Logik NOT
# 12. and                                          - Logik AND
# 13. or                                           - Logik OR