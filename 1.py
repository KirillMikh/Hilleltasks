class MyRange:
    def __init__(self, stop, start=0, step=1):
        if start == 0:
            self.start = start
            self.stop = stop
            self.step = step
        else:
            self.start = stop
            self.stop = start
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):

        if self.start >= self.stop:
            raise StopIteration

        self.start += self.step
        return self.start - self.step


for i in MyRange(20):
    print(i, end=' ')
print("\n")
for i in MyRange(4, 20):
    print(i, end=' ')
print("\n")

for i in MyRange(5,20,5):
    print(i, end=' ')
print("\n")


def my_generator(stop, start=0, step=1):
    if start != 0:
        start, stop = stop, start
    while start < stop:
        yield start
        start += step


for i in my_generator(20):
    print(i, end=" ")
print("\n")
for i in my_generator(4, 20):
    print(i, end=" ")
print("\n")

for i in my_generator(5,20,5):
    print(i, end=" ")
print("\n")
