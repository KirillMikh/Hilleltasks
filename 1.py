class MyRange:
    def __init__(self, *args):
        tuple1 = tuple(args)
        self.start = 0
        self.step = 1
        if len(tuple1) == 1:
            self.stop = tuple1[0]
        elif len(tuple1) == 2:
            self.start, self.stop = tuple1
        elif len(tuple1) == 3:
            self.start, self.stop, self.step = tuple1

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            raise StopIteration
        elif self.start<=self.stop and self.step<0 or self.start>=self.stop and self.step>0:
            raise StopIteration

        self.start += self.step
        return self.start - self.step


for i in MyRange(20):
    print(i, end=' ')
print("\n")
for i in MyRange(7, 20):
    print(i, end=' ')
print("\n")

for i in MyRange(20, 5,-5):
    print(i, end=' ')
print("\n")

for i in MyRange(5, 20,5):
    print(i, end=' ')
print("\n")

for i in MyRange(2, 7, 0):
    print(i, end=' ')
print("\n")


def my_generator(*args):
    tuple1 = tuple(args)
    start = 0
    step = 1
    if len(tuple1) == 1:
        stop = tuple1[0]
    elif len(tuple1) == 2:
        start, stop = tuple1
    else:
        start, stop, step = tuple1
    while start > stop and step < 0 or start < stop and step > 0 and step!=0:
        yield start
        start += step


for i in my_generator(20):
    print(i, end=" ")
print("\n")
for i in my_generator(7, 20):
    print(i, end=" ")
print("\n")

for i in my_generator(20, 5, -5):
    print(i, end=" ")
print("\n")

for i in my_generator(5, 20, 5):
    print(i, end=" ")
print("\n")
for i in my_generator(2,7,0):
    print(i, end=" ")
print("\n")



