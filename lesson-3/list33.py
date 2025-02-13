numbers = [1, 2, 3, 4, 5, 2, 6, 7, 2]
element = 2

indices = []
for i in range(len(numbers)):
    if numbers[i] == element:
        indices.append(i)
print(indices)   