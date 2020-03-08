
import math

class Figure:
    def P(self):
        raise Exception("No")

    def S(self):
        raise Exception("No")


class Triangle(Figure):
    def __init__(self,list1:list):
        if len(list1) != 3:
            raise Exception("не 3 стороны")
        self.a = list1[0]
        self.b = list1[1]
        self.c = list1[2]

    def P(self):
        return self.a+self.b+self.c


    def S(self):
        p = self.P()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Rectangle(Figure):
    def __init__(self, list1: list):
        if len(list1) != 2:
            raise Exception("не 2 стороны")
        self.a = list1[0]
        self.b = list1[1]

    def P(self):
        return self.a * 2 + self.b * 2

    def S(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def P(self):
        return format(2*math.pi*self.r)


    def S(self):
        return math.pi*self.r**2



t1 = Triangle([3, 4, 5])
print(t1.P())
print(t1.S())

rec1 = Rectangle([10, 25])
print(rec1.P())
print(rec1.S())

c = Circle(5)
print(c.P())
print(c.S())

