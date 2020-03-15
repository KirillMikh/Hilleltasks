def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except:
            return None
        return result

    return wrapper


class Exception_handler:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


@exception_handler
def func1(a):
    x = 1/a
    print(x)


def func2(a):
    x = 2 / a
    print(x)


func1(0)#ошибка подавляется
func1(10)#функия отработала


with Exception_handler():   #ошибка подавляется
    func2(0)

with Exception_handler():   #функция отрабатывает
    func2(2)

