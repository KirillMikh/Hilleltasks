from functools import wraps


def decorator_function_docString(func):
    """докстринг декоратора, принимает функцию"""

    @wraps(func)
    def wrapper(a):
        """докстринг функции- обертки"""
        return "The result is "+ str(func(a))

    return wrapper


@decorator_function_docString
def my_function(x):
    """моя элэментарная функция"""
    return x*2


print(my_function(16))
print(my_function.__doc__)
print(my_function.__name__)
# c помощью wraps получается избежать перезаписи докстринга и названия  обертываемой функции
# на докстринг и название обертки
