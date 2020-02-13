l = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]


def function1(list1):
    dict1 = dict()
    count = 1
    for element in range(len(l)-1):
        if list1[element] == list1[element+1]:
            count += 1
        if count >= int(dict1.get(list1[element], 0)):
            dict1[list1[element]] = count
        if list1[element] != list1[element+1]:
            count = 1
    max_dict1 = max(dict1.values())
    for key in dict1:
        if dict1[key] == max_dict1:
            return key, max_dict1


print(function1(l))
