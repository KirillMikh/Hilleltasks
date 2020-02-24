a=open("file1","w")
a.write("hfgfhfh cnh fnhcb sdskdj  skd sdfg sdsd \nsidsd sdsd qqqqqqq cgvcv cmvncmvn")
a.close()



b=open("newfile1","w")
b.close()


a=open("file1","r")

counter=0

index_list=[]
line=a.readline()
while line:
    list1=line.split(" ")
    for word in range(len(list1)):
        if len(list1[word])<=5 or len(list1[word])>=3:
           index_list.append(1)
           temp=word
        else:
            index_list.append(0)
    if sum(index_list)%2==1:
        index_list[temp]=0
    for word in range(len(list1)):
        if index_list[word]==0:
            b = open("newfile1", "a")
            b.write(list1[word]+" ")
            b.close()
        b = open("newfile1", "a")
        b.write("\t")
        b.close()
    line = a.readline()
a.close()