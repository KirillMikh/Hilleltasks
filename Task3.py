list1 = [["Krishna", 67, 68, 69], ["Arjun", 70, 98, 63], ["Malika", 52, 56, 60]]
dict1 = {}
for i in range(len(list1)):
    dict1.update({list1[i][0] : (sum(list1[i][1:])/3) })
while True:
    str1 = input("Введите имя")
    print(dict1.get(str1))
