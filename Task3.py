list1 = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1, 2], {1: 1}]
set1 = set()
dict1 = dict()
common_type_number = 0
common_type = ""
for element in list1:
    tp = str(type(element))
    if tp not in set1:
        set1.add(tp)
        dict1[tp] = 1
    else:
        dict1[tp] = dict1.get(tp, 0) + 1
        if common_type_number <= dict1.get(tp):
            common_type_number = dict1.get(tp)
            common_type = tp
print (dict1)
print("Самый часто встречаемы объект " + common_type)
for element in list1:
    if str(type(element)) == common_type:
        print(element)

