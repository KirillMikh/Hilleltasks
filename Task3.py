str1 = input("Введите строку ")
list1 = list(str1)
for i in range(len(list1)):
    if list1[i] != list1[len(list1)-i-1]:
        print(" слово не является палиндромом")
        break
    elif i == len(list1)-1:
        print(" слово  является палиндромом")

