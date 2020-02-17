def one_call_counter(func):
    called = False

    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            print('первая инициализация')
            func(*args, **kwargs)
            called = True
        else:
            print('не первая инициализация')
            func(*args, **kwargs)
    return wrapper


@one_call_counter
def function1(x):
    print('I am function', x)

#если функция уже вызывалась то она все же выполняется, но текст перед ее выполнением указывает на не первую иницализацию
function1(1)
function1(2)
function1(3)