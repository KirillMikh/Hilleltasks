import collections
list1 = [1, 2, 3, 4, 5, 6, 7]
print("Изначальный список(0 -выход из вечного цикла) : ", list1)
step = 1
while step != 0:
    step = int(input("Введите число сдвига(больше 0 -вправоб меньше 0 -влево)"))
    if step > 0:
        for i in range(step):
            list1.insert(0, list1.pop(len(list1)-1))
    elif step < 0:
        for i in range(abs(step)):
            a = list1.pop(0)
            list1.append(a)
    print("Измененный список", list1)
# Реализация с помощью deque
print("Изначальный список (deque)", list1)
deque1 = collections.deque(list1)
step2 = 1
while step2 !=0:
    step2 = int(input("Введите число сдвига больше 0 -вправоб меньше 0 -влево"))
    deque1.rotate(step2)
    print("Измененный список", deque1)


