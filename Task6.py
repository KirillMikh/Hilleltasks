str1 = "English = 78 Science = 83 Math = 68 History = 65"
words_list = str1.split(" ")
sum = 0
for word in words_list:
    if word.isdecimal():
        sum += int(word)
print(sum)
