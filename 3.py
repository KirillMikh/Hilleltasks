import time


class MyClass:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("Время выполнения (Контекст)= " + str(end-self.start))


    def __call__(self, func):
        self.func = func

        def wrapper(*args,**kwargs):
            start = time.time()
            result = self.func(*args,**kwargs)
            end = time.time()
            print("Время выполнения (Декоратор)=  " + str(end-start))
            return result
        return wrapper

#реализация через декораторы

@MyClass()
def my_function1():
    a = 0
    for i in range(3_000_000):
        if a != 0:
             b= 1 / a
@MyClass()
def my_function2():
    a = 0
    for i in range(3_000_000):
        try:
              1 / a
        except Exception:
            pass


my_function1()
my_function2()

#реализация через контекст
a = 0
with MyClass() :
    for i in range(3_000_000):
        if a != 0:
            b= 1 / a

with MyClass():
    for i in range(3_000_000):
        try:
           1 /a
        except ZeroDivisionError as e:
            pass
#вывод -if работает быстрее