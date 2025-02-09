text = input("Enter a string: ")
vowels = "aeiouAEIOU"

result = "".join('*' if char in vowels else char for char in text)

print("String after replacement:", result)
