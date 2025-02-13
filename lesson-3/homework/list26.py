numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = len(numbers)

if num % 2 != 0:
    a = num //2
    print(numbers[a])
elif num % 2 == 0:
    b = num // 2 - 1
    c = num // 2 
    print(numbers[b], numbers[c])
