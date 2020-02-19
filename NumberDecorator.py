def decoratot_number(func):
    def wrapper(listq):
        list2=[]
        for i in listq:
            list2.append("+91 "+ str(i[len(i)-10:len(i)-5])+" "+ str(i[len(i)-5: ]))
        return list2
    return wrapper

@decoratot_number
def sort_function(list1):
    return list1.sort()



def input_number():
    str1 = int(input("Введите число - количество номеров "))
    list1 = []
    for i in range(str1):
        list1.append(input("Введите " + str(i + 1) + " номер"))
    print(*sort_function(list1),sep="\n")

input_number()