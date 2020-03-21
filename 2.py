def decorator_maker(*args):
    errors_tuple = args

    def exception_handler(func):
        def wrapper(*args1):
            try:
                result = func(*args1)
            except errors_tuple:
                return print("Возникла ошибка но была подавлена")
            return result
        return wrapper
    return  exception_handler


@decorator_maker(ZeroDivisionError, TypeError)
def f1(a):
    if a == 1:
        print(2131 + "string")
    else:
        print(1/0)

@decorator_maker(IndexError)
def f2():
    print([][5])

f1(1)
f1(2)
f2()

