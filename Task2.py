list1 = [21, 10, 5, 7, 2, 4, 11, 4,1]
list1.sort()
print(list1)
if len(list1)%2 ==1:
    print("Медиана= "+str(list1[len(list1)//2]))
else:
     print("Медиана= "+str((list1[len(list1) // 2]+list1[(len(list1) // 2)-1])/2))
