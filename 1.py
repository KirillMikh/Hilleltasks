class StaticMethod:

    def __init__(self, instance):
        self.instance = instance
        # print(self.__dict__)
        # print(type(instance))

    def __get__(self, instance, owner):
        return self.instance


class MyClass1:
    @StaticMethod
    def foo1(a1):
        return 10+a1


a = MyClass1()
print(a.foo1(13))
print(MyClass1.foo1(13))


class ClassMethod(object):
    def __init__(self, method):
        self.method = method
    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)
        def func1(*args):
            return self.method(owner, *args)
        return func1

class MyClass2:

    @ClassMethod
    def foo1(cls,param1):
       print (param1,cls)


a2 = MyClass2()
a2.foo1(5)
MyClass2.foo1(5)









