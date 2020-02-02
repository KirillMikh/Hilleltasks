import random
list1 = []
for i in range(100):
    list1.append(random.randint(1, 10000))
list1.sort()
print("Отсортированый список, 100 элементов от 1 до 10000: \n", str(list1))
lower_bound = 0
upper_bound = list1.__len__()-1
number = int(input("Введите число от 1 до 1000:  "))
while lower_bound <= upper_bound:
    middle = (lower_bound + upper_bound) // 2
    if number < list1[middle]:
        upper_bound = middle - 1
    elif number > list1[middle]:
        lower_bound = middle + 1
    else:
        print("Позиция искомого числа(начиная с 1)", middle+1)
        break
else:
    print("Введенного числа нет в списке")


