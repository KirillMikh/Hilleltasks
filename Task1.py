list1 = [
	[1, 2, 3, 4, 5, 6],
	[10, 21, 13, 14, 52, 63, 34],
	[2],
	[3, 2, 6],
	[35, 47],
	[-3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
	[100, 200, 300, 400, 500, 600]
]
i = 0
for element in list1:
	count = 0
	for number in element:
		if number % 2 == 1:
			count += number
	i += 1
	print("сумма нечетных чисел в строке номер " + str(i) + " равняется "+ str(count))

