num = int(input("Enter the number: "))

if num % 3 == 0 and num % 5 ==0:
    print(f"The {num} is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")