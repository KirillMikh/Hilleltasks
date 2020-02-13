def min_search(*args):
    min1 = args[0]
    for i in args:
        if min1 > i:
            min1 = i
    return min1


print(min_search(90, 13, 4, 78, 5, -20, -2))

