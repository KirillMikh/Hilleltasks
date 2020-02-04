import heapq
list1 = [4, 59, 56, 1, 2, 45, 90, 3, 5, 6, 7, -21, 789,-120]
heapq.heapify(list1)
list1 = [heapq.heappop(list1) for i in range(len(list1))]
print("Отсортированный список", list1)