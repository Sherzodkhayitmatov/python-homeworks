text  = input("Enter the text: ")
num_digit = 0

for num in text:
    if num.isdigit():
        num_digit += 1
        
print(num_digit)