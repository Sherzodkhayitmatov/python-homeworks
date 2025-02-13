set1 = {1, 2, 3}
num = 1

if num in set1:
    print("There is a such number")
else:
    set1.add(num)
    print("Added")
    print(set1)