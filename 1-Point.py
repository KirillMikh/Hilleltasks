import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def square(self,other):
        side1=self.y
        side2=other.y
        middleLine=(side1+side2)/2
        h1=abs(self.x-other.x)
        return h1*middleLine

    def distance(self,other):
        katet1=abs(self.y-other.y)
        katet2=abs(self.x-other.x)
        return math.sqrt(katet1**2+katet2**2)


p1=Point(3,5)
print(p1.square(Point(5,8)))
print(p1.distance(Point(5,8)))
