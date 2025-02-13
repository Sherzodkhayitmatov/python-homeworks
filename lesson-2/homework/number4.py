num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

answer = round(num1 // num2, 0)
rounded_num = num1 % num2
print(f"Result is {answer}.")
print(f"Remainder is {rounded_num}.")