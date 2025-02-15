print("Input:")
list1 = list(input("list1= "))
list2 = list(input("list2= "))
uncommon_list = []

for i in list1:
    if i not in list2:
        uncommon_list.append(i)
for j in list2:
    if j not in list1:
        uncommon_list.append(j)
print(uncommon_list)