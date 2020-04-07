a = open("file1.txt", "w")
a.write("i want to go home\n"
        "bla bla bla\n"
        "i want to go home\n"
        "she is Mary\n"
        "he is Carl\n"
        "bla bla bla")
a.close()


def string_generator(filename):
    set1 = set()
    f1 = open(filename, "r")
    line = f1.readline()
    line=line.strip()
    while line:
        if line not in set1:
            set1.add(line)
            yield line
        line = f1.readline()
        line= line.strip()
    f1.close()


a1 = string_generator("file1.txt")
for i in a1:
    print(i)





