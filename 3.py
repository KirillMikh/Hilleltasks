
class Emails:

    def __init__(self, email):
        self.email = email

    class EmailDescriptor:
        def __get__(self, instance, owner):

            return instance._email

        def __set__(self, instance, value:str):

            if '@' in value:
                str1 = value.split("@")
                if len(str1[0])>0 and len(str1[1])>0:
                    instance._email = value
                    print('value changed on ', value)
                else:
                    raise Exception('Неправильный новый электронны адрес')
            else:
                raise Exception('Неправильный новый электронны адрес')


    email = EmailDescriptor()


email1 = Emails("validemail@gmail.com")
print(email1.email)
email1.email = "mynewemail@ukr.net"#не вызовет исключения
email1.email = "cvbf@"#вызовет исключение, последний символ собачка
