str1 = input("Введите строку ")
list1 = list(str1)
list2 = list1
list2.reverse()
if list1 == list2:
    print(" слово является палиндромом")
else:
    print(" слово не является палиндромом")

