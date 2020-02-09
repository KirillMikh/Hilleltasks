password = "assasasas"


def validator(str1):
    if len(str1) <= 4:
        return "Строка не является валидным паролем, длина меньше или равно 4"
    count_letters = 0
    count_digits = 0
    for i in str1:
        if i.isascii() and i.islower():
            count_letters += 1
        elif i.isdigit():
            count_digits += 1
        else:
            return "Строка не является валидным паролем, запрещенные символы"
    if (count_letters % 2 == 0) or (count_digits % 2 != 0):
        return "Строка не является валидным паролем "

    return "Строка является валидным паролем, количество маленьких латинских букв " + str(count_letters)+", количество цифр " +str(count_digits)


print(validator("qwert1222"))
print(validator("фбгвда1"))
print(validator("POl123"))
print(validator("qwert1"))
print(validator("hello45"))