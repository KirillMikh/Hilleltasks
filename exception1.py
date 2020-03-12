import traceback
class MyException(Exception):
    def __init__(self,text):
        self.text=text



    def write_to_file(self):
        a=open("fileErrors",'w')
        a.write(self.text+'\n')
        traceback.print_tb(self.__traceback__,file=a)
        a.close()



try:
    raise MyException("Error occured")
except MyException as error:
    error.write_to_file()


