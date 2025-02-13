numbers = [1, 2, 4, 4, 2, 9]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)