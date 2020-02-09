list2 = [1, 2, 3, 4, 5, 6]


def function2(list1):
    bits_element_sum = 0
    for i in range(len(list1)):
        str1 = str(bin(i))
        if str1.count("1") % 2 == 0 :
            bits_element_sum += list1[i]
    return bits_element_sum * list1[-2]


print(function2(list2))




