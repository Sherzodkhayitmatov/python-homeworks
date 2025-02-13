set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}

new_set = list(set(set1) | set(set2))
print(new_set)