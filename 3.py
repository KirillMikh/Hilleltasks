def solve(s: str):
    temp =""
    if s[0].isalpha():
        temp+=s[0].upper()
    else:
        temp+=s[0]
    for i in range(len(s))[0:len(s)-1]:

        if s[i+1].isalpha() and s[i].isspace():
            temp += s[i+1].upper()
        else:
            temp += s[i+1]
    return temp

print(solve("12abc kirill mikhalev"))