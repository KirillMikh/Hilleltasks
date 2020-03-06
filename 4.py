import os
import  json


class JsonHandler:


    @staticmethod
    def writeToFile(info,filename:str):
        a1 = open(filename, 'w')
        json.dump(info, a1)
        a1.close()

    @staticmethod
    def readFromFile(filename:str):
        a2 = open(filename, 'r')
        line = a2.readline()
        while line:
            print(line)
            line = a2.readline()
        a2.close()


    @staticmethod
    def filesToOne(filenames: list):
        d1 = dict()
        for file in filenames:
            a3 = open(str(file),'r')
            d1.update(json.load(a3))
            a3.close()
        file1 = open("mergedfile.json", "w")
        json.dump(d1, file1)
        file1.close()


    @staticmethod
    def get_absolute_path(filename: str):

        return os.path.abspath(filename)


    @staticmethod
    def get_relative_path( filename: str):

        return os.path.relpath(filename)



data1 = {1:12, 13:(1, 2)}
data2 = {5: 'asas', 55: "hello", 3: "cool"}

a1 = open("file1.json", "w")
json.dump(data1, a1)
a1.close()

a2 = open("file2.json","w")
json.dump(data2, a2)
a2.close()

data3 = {14:1000, 13:9000,8:1212}

JsonHandler.writeToFile(data3,"file1.json")

JsonHandler.readFromFile("file1.json")
JsonHandler.readFromFile("file2.json")

JsonHandler.filesToOne(['file1.json', 'file2.json'])#появляется новый файл в текущей директории


print(JsonHandler.get_absolute_path('file1.json'))


print(JsonHandler.get_absolute_path('file3.json'))
print(JsonHandler.get_relative_path('file3.json'))