list1 = [1,2,3,4,5,6]
list2 = [1,2,3]
if any(list1[i:i+len(list2)] == list2
       for i in range(len(list1) - len(list2) + 1)):
    print("It exists")
else:
    print("It does not exit")