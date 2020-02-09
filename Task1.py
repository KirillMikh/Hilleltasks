list1 = [1, 2, 3, 4, 5, 6, 7, 8, 89, 23, 4, 5]
print(list1)


def swap(target_list, item_index1, item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    return list1


print(swap(list1, 3, 6))
