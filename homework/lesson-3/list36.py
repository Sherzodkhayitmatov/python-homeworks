numbers = [1, -2, -3, 4, 5, -6, 7]
positive = []
for i in numbers:
    if i > 0:
        positive.append(i)
print(sum(positive))