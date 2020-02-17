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
            for key in dict_values:
                if tmp == dict_values.get(key):
                    return key

        if args in dict_values and len(dict_values) < cache_size:
            deque1.remove(dict_values.get(args))
            deque1.appendleft(dict_values.get(args))
            cache_calls += 1
            return dict_values.get(args)
        elif args in dict_values and len(dict_values) == cache_size:
            tmp1 = deque1.pop()
            deque1.appendleft(dict_values.get(args))
            cache_calls += 1
            return tmp1
        elif len(dict_values) < cache_size and args not in dict_values:
            calls += 1
            temp = my_func(args)
            dict_values[args] = temp
            deque1.appendleft(temp)
            return temp
        elif len(dict_values) == cache_size and args not in dict_values:
            temp1 = time_check()
            dict_values.pop(temp1)
            calls += 1
            temp = my_func(args)
            dict_values[args] = temp
            deque1.appendleft(temp)
            return temp

    def cache_info():
        nonlocal cache_calls
        nonlocal calls
        nonlocal cache_size
        print("Функция вычислялась раз: " + str(calls) + " совободного места "+str(cache_size - len(dict_values))
              + " значений было взято из кэша раз " + str(cache_calls))

    def cache_clear():
        nonlocal cache_calls
        nonlocal calls
        calls = 0
        cache_calls = 0
        dict_values.clear()
        deque1.clear()

    wrapper.cache_clear = cache_clear
    wrapper.cache_info = cache_info
    return wrapper


@my_lru_cache
def my_function(x):
    return x


a = my_function
#описание работы и наглядный пример :)
for i in range(100):#
    a(i)
a.cache_info()#сейчас сработала функция 100 раз в кэш записалось 100 значений от 0 до 100
for i in range(50):
    a(i)   #эти значение уже есть в кэшэ, функция повторно не вычисляется, происходит обращение к кэшу
a.cache_info()
for i in range(50):
    a(i) #эти значение уже есть в кэша, функция повторно не вычисляется, происходит повторное  обращение к кэшу
a.cache_info()
for i in range(250):
    a(i) # появляются новые значения но 100 первых из них уже есть в кэше поэтому идет запрос 100  значений
    # и 150 еще вычисляются причем при перезаполнении кєша самые старые значения удаляются
a.cache_info()
for i in range(50, 250):
    a(i) # сейчас в кэше 200 значений от 50 до 250(200 последниx после выполнения предыдущего цикла)
    # и поэтому сейчас идет обращение  к кешу и функция не вычисляется
a.cache_info()

a.cache_clear()#очищаем кэш
a.cache_info()# вся статистика сбрасывается