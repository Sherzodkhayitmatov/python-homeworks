a = int(input("Enter the first number: "))

if a > 0:
    if a % 2 == 0:
        print("Number is positive and even.")
    else:
        print("Number is positive, but not even.")
else:
    print("Number is not positive.")