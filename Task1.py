list1 = [
	[1, 2, 3, 4, 5, 6],
	[10, 21, 13, 14, 52, 63, 34],
	[2],
	[3, 2, 6],
	[35, 47],
	[-3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
	[100, 200, 300, 400, 500, 600]
]
list_sums = []
for element in list1:
	list_sums.append((sum(i for i in element if i % 2 == 1)))
print(*list_sums,sep="\n")
