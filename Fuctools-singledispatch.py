from functools import singledispatch


@singledispatch
def my_function(arg, typeDisplay=False):  # будет вызываться по дефолту
    if typeDisplay:
        print('some type')
    print('arg is: ', arg)


@my_function.register
def _(arg: int, typeDisplay=False):
    if typeDisplay:
        print('Function argument is int')
    print('arg is: ', arg)


@my_function.register
def _(arg: list, typeDisplay=False):
    if typeDisplay:
        print('Function argument is list')
    print('arg is: ', arg)

@my_function.register
def _(arg: float, typeDisplay=False):
    if typeDisplay:
        print('Function argument is float')
    print('arg is: ', arg)

@my_function.register
def _(arg: bool, typeDisplay=False):
    if typeDisplay:
        print('Function argument is bool')
    print('arg is: ', arg)


my_function([1,2,3],True)
my_function(560,True)
my_function(20.45,True)
my_function(True,True)