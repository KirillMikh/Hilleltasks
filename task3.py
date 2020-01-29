a = 5656
count = 0
i = 2
while i < a:
    if a % i == 0:

        a = a/i
        count = count+1
    else:
        if count > 1:
            print(str(i), '^', str(count) + ' * ', end="")
        if count == 1:
            print(str(i), ' * ', end="")

        i += 1
        count = 0
if a == i:
    count=count+1
if count > 1:
    print(str(i), '^', str(count) + '  ', end="")
if count == 1:
    print(str(i), '  ', end="")


