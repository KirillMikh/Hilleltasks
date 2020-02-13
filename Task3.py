str1 = "Hello I am Kirill!"


def upperLetter_search(str1):
    str2 = []
    for i in str1:
        if i.isupper():
            str2.append(i)
    print("".join(str2))


upperLetter_search(str1)
