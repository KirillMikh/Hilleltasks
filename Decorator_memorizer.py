import time


def my_timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print('Execution time: ', format(time.time() - t))
        return res
    return tmp


def memorizer(f):
    cache = {}
    def decorate(*args):
        print(args)

        if args not in cache:
            print('args not in cache')
            cache[args] = f(*args)
            print(cache.keys())
        return cache[args]
    return decorate

@my_timer
@memorizer
def my_function(x,y):
    list1 = []
    for i in range(y):
        if i % 2 == 0:
            list1.append(x+i)
    return list1


my_function(126, 10_000)

my_function(720, 900_000)

my_function(720, 900_000)

my_function(720, 900_000)


