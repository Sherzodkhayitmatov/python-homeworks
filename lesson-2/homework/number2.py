num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
num3 = int(input("Write the second number: "))

if num1>num2:
    if num1>num3:
        print(f"The largest number: {num1}")
    elif num3>num2:
        print(f"The smallest number: {num2}")
    else:
        print(f"The smallest number: {num3}")
        
if num2>num1:
    if num2>num3:
        print(f"The largest number: {num2}")
    elif num3>num1:
        print(f"The smallest number: {num1}")
    else:
        print(f"The smallest number: {num3}")
        
if num3>num1:
    if num3>num2:
        print(f"The largest number: {num3}")
    elif num2>num1:
        print(f"The smallest number: {num1}")
    else:
        print(f"The smallest number: {num2}")
        