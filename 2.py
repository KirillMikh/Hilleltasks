
def exception_handler(func,*args):
    errors_tuple = args

    def wrapper(*args1):
        try:
            result = func(*args1)
        except errors_tuple:
            return print("Возникла ошибка но была подавлена")
        return result
    return wrapper


def f1(a):
    if a == 1:
        print(2131 + "string")
    else:
        print(1/0)


def f2():
    print([][5])


def f3():
    a = open("sdsdsdsq12a79852142321212","r")
    a.close()


f1 = exception_handler(f1, ZeroDivisionError, TypeError)
f1(1)
f1(2)

f2 = exception_handler(f2, IndexError)
f2()


#Здесь возникнет ошибка, потому что тип ошибки которую надо подавить-FileNotFound
# f3= exception_handler(f3, TypeError)
# f3()