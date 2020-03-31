class ReverseIterator:

    def __init__(self, collection):
        self.collection = collection
        self.index = len(collection)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]


list1 = ["hello", 8, 9, 10, 11, 12, 13, 14, 15, (123, 54), (90, 100)]
it1 = ReverseIterator(list1)


print(list(ReverseIterator(list1)))

for a in it1:
    print(a)
