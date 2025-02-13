def isTrue(numbers, sorted_num):
    if numbers == sorted(sorted_num):
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7]
sorted_num = sorted(numbers)
print(isTrue(numbers, sorted_num))
