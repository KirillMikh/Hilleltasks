def zip_generator(*args):
    min_collection = min([len(arg) for arg in args])
    args = [tuple(i) for i in args]
    for index in range(min_collection):
        yield tuple(collection[index] for collection in args)


set1 = {49, 44, 490, 'i am here', 'bla bla bla'}#у сетов будет брать каждый раз
set2 = {49, 44, 490,'bla bla bla'}#случайные элементы из-за внутренней логики расположения элементов
list1 = ['a', 'b', 'b', 'c']
tuple1 = (123, 121, 87878)
list2 = [1, 2, 3, 4, 5]
dict1={'dictkey1':11, 'dictkey2':22}



a = zip_generator(list1,dict1)
for i in a:
    print(i)

print('\n')

a = zip_generator(set1,set2)
for i in a:
    print(i)

print('\n')

a = zip_generator(list1, list2, tuple1)
for i in a:
    print(i)
