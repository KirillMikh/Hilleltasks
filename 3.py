str1=input("")
name= str1.title()
temp=""
list1=[]
for i in str1:
    if not i.isspace():
        temp +=i
    elif i.isspace():
        list1.append(temp)
        temp=""
list1.append(temp)
list2=[]
for i in list1:
    if not i[0].isdigit():
        list2.append(i.capitalize())
    else:
        list2.append(i)
print(" ".join(list2))
# for i in str1:
#     if i==0 orkirill mikh