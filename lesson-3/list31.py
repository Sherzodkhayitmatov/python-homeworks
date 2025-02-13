numbers = [1, 2, 3, 4, 5, 6, 7]
num = 2
new_list = [ i for i in numbers  for _ in range(num)
]
print(new_list)