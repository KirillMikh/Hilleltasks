list1 = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 1, 2]


def create_rle(list1):
    list2 = []
    count = 1
    for i in range(len(list1)-1):
        if list1[i] == list1[i+1]:
            count += 1
        if list1[i] != list1[i+1]:
            list2.append({list1[i]: count})
            count = 1
    list2.append({list1[len(list1)-1]: count})
    return list2

#cначала значение потом сколько раз
print(create_rle(list1))
