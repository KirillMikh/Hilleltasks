string1 = "spam and eggs or eggs with spam"
list1 = list(string1)
set1 = set(string1)
dict1 = {}
for symbol in set1:
    dict1[symbol] = list1.count(symbol)
print(dict1)
