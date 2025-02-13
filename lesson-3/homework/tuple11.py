a = (1, 2, 3, 2, 3, 1, 3, 4, 3)
element = 3

indices = []
for i in range(len(a)):
    if a[i] == element:
        indices.append(i)
print(indices)
