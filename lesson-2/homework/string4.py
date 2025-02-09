text = input("Enter the text: ")
if text.lower() == text.lower()[::-1]:
    print(f"{text} is palindrome.")
else:
    print("Text is not palindrome.")