import functools


def singleton1(cls):
    classes = dict()
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in classes:
            classes[cls] = cls(*args, **kwargs)
        return classes.get(cls)

    return wrapper


@singleton1
class Class1:
    pass


@singleton1
class Class2:
    pass

a1=Class1()
a2=Class1()

b1=Class2()
b2=Class2()
print(id(a1),id(a2))
print(id(b1),id(b2))

