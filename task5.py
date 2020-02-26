import string


def rangoli_maker(size:int):
    all_letters = string.ascii_lowercase
    a = size
    letters = all_letters[0:a]
    str1 = list()
    line_length = 4*a-3
    for i in range(a):
        temp_str = "-".join(reversed(letters[i:a]))
        if len(letters[i+1:a]) < 1:
            temp_str = temp_str+"-".join(letters[i+1:a])
        else:
            temp_str = temp_str + "-" + "-".join(letters[i + 1:a])
        str1.append(temp_str.center(line_length, "-"))

    print(*reversed(str1[1::]), *str1, sep="\n")

rangoli_maker(5)
