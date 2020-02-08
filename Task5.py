import random
allowed_symbols = []
for symbol in range(ord("0"), ord("9") + 1):
    allowed_symbols.append(chr(symbol))
for symbol in range(ord("a"), ord("z") + 1):
    allowed_symbols.append(chr(symbol))
for symbol in range(ord("A"), ord("Z") + 1):
    allowed_symbols.append(chr(symbol))
str1 = "1"
while str1.isdecimal():
    str1 = input("Введите длину пароля")
    while not str1.isdecimal():
       str1 = input("Ошибка, Введите число")
    if int(str1) == 0:
        exit(0)
    password = ""
    for symbol in range(int(str1)):
        password += random.choice(allowed_symbols)
    print("Ваш пароль: ", password)
