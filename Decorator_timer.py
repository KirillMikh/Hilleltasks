import time


def my_timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print('Execution time: {}'.format(time.time() - t))
        return res
    return tmp


@my_timer
def even_count(limit):
    list1 = []
    for i in range(limit):
        if i % 2 == 0:
            list1.append(i)
    return list1


even_count(1000000)

