# #2.1
dict1 = {'a': 1, 'b': 4, 't': 67}
dict2 = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

set1 = set(dict1.keys())
set2 = set(dict2.keys())
set1.intersection_update(set2)
print("Ключи, которые есть в обоих словарях: ", set1)
#2.2

set1 = set(dict1.keys())
print(set1,set2)
set2.difference_update(set1)
print("Ключи которые есть только во 2м словаре, но нет в 1м ", set2)

#2.3
dict3 = {}
set1 = set(dict1.keys())
set2 = set(dict2.keys())
set1.update(set2)

for key in set1:
    dict3[key] = dict1.get(key, 0) + dict2.get(key, 0)
print("объединить словари в один, так чтоб числа при одинаковых ключах суммировались ", dict3)


