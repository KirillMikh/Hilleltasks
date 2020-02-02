#1.1
list1 = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print("Максимальное значение " + str(max(list1)))
print("Индекс максимального значения " + str(list1.index(max(list1))))
print("Минимальное значение " + str(min(list1)))
print("Индекс минимального значения " + str(list1.index(min(list1))))
#1.2
set1 = set(list1)
numbers = []
for i in range(3):
    most_common_number = None
    frequency = 0
    for number in set1:
        temp_number = list1.count(number)
        if temp_number > frequency:
            frequency = temp_number
            most_common_number = number
    set1.remove(most_common_number)
    numbers.append(most_common_number)
print("три самых часто встречаемых элемента массива", numbers)
#1.3
list2 = list(set(list1))


print("преобразованый список где каждый елемент встречаетс по 1 разу с сохранением порядка", list2)
set2 = set()
list3 = []
for i in list1:
    if not set2.__contains__(str(i)):
        set2.update(str(i))
        list3.append(i)
print("преобразованый список где каждый елемент встречаетс по 1 с сохранением порядка", list3)
