a=open("numberlist1",'w')
a.write("12345678\tKali\n")
a.write("00012223\tLara\n")
a.write("12940237\tSam\n")
a.write("90297381\tKendall\n")
a.write("77788877\tCasha")
a.close()

a=open("numberlist1",'r')
b=open("newfile1","a")


line =a.readline()
while line:
    if line.split("\t")[1][0] in ("C","K"):
        print(line.split("\t")[1][0])
        b.write(line)
    line=a.readline()

a.close()
b.close()




