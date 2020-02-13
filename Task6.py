''' Реализовано для большого списка(1000000) значения но для небольшого количества вызовов (100)'''
from random import randint
list1 = list(range(1000000))


def sum_search(args):
    for arg in args:
        print(sum(list1[arg[0]:arg[1]+1]))


list3 = []
[list3.append([randint(1, 500000), randint(500000, 1000000)]) for i in range(100)]
sum_search(list3)


