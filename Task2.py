str = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = int(input("Введите число символов в строке"))
for i in range(0, len(str), w):
    print(str[i:i+w])

