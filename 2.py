# import functools
# list1 = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]
#
# #
# # def create_list(list1):
# #     list2 = []
# #     def open_list(list1):
# #         for i in list1:
# #             if isinstance(i, list):
# #                 open_list(i)
# #             else:
# #                 list2.append(i)
# #     open_list(list1)
# #     return list2
# #
# #
# # print(create_list(list1))
# functools.reduce(lambda cumm,x:cumm.append(x), list1)

import collections
from functools import wraps
def my_lru_cache(my_func):
    dict_values = dict()
    cache_size = 200
    cache_calls = 0
    deque1 = collections.deque([])
    calls = 0
    @wraps(my_func)
    def wrapper(*args):
        nonlocal cache_calls
        nonlocal dict_values
        nonlocal cache_size
        nonlocal deque1
        nonlocal calls
        def time_check():
            tmp = deque1.pop()
            for i in dict_values:
                if tmp == dict_values.get(i):
                    tmp2 = i
            dict_values.pop(tmp2)

        if dict_values.get(args, False):
                # deque1.remove(args)
                deque1.appendleft(args)
                cache_calls += 1
                return dict_values.get(args)
        elif len(dict_values) < cache_size:
            calls += 1
            temp = my_func(args)
            dict_values[args] = temp
            deque1.appendleft(temp)
            return temp
        elif len(dict_values) >= cache_size:
            time_check()
            calls = +1
            temp = my_func(args)
            dict_values[args] = temp
            deque1.appendleft(temp)
            return temp

    def cache_info():
        nonlocal cache_calls
        nonlocal calls
        nonlocal cache_size
        print("Функция вычислялась раз: " + str(calls) + " совободного места "+str(cache_size - len(dict_values))
              + " значений было взято из кэша " + str(cache_calls))

    def cache_clear():
        nonlocal cache_calls
        nonlocal calls
        wrapper.calls = 0
        cache_calls = 0
        dict_values.clear()
        deque1.clear()

    wrapper.cache_clear = cache_clear
    wrapper.cache_info = cache_info
    return wrapper


@my_lru_cache
def my_function(x):
    return 2+7



for i in range(50):
    my_function(i)


my_function.cache_info()

for i in range(50):
    my_function(i)

my_function.cache_info()


my_function.cache_clear()
my_function.cache_info()