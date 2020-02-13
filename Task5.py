list1 = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]


def create_list(list1):
    list2 = []
    def open_list(list1):
        for i in list1:
            if isinstance(i, list):
                open_list(i)
            else:
                list2.append(i)
    open_list(list1)
    return list2


print(create_list(list1))