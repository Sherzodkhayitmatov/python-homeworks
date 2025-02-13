tup = (1, 2, 3)
n = 2
result = tuple([x for x in tup for _ in range(n)])
print(result)
