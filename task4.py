a = open("file1","w")
a.write("kate want to eat some  burgers \n"
        "she went to the store and bought a couple \n"
        "such a good weather outside today\n"
         )
a.close()

b=open("newfile1","w")
b.close()
a=open("file1","r")


index_list=[]
line=a.readline()
while line:
    list1=line.split(" ")
    print(list1)
    for word in range(len(list1)):
        if 5 >= len(list1[word]) >= 3:
           index_list.append(1)
        else:
            index_list.append(0)
    if sum(index_list) %2 == 1 and sum(index_list)>0:
        last_one=len(index_list) - 1 - index_list[::-1].index(1)
        index_list[last_one] = 0

    b = open("newfile1", "a")
    for word in range(len(list1)):
        if index_list[word] == 0:
            b.write(list1[word])
            if word != len(list1)-1:
                b.write(" ")
    b.close()
    index_list.clear()
    line = a.readline()
a.close()
