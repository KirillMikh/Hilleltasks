str1 = input("Введите строку")
list1 = str1.split(" ")
for i in range(len(list1)):
    print(list1[i][::-1], " ", end="")
