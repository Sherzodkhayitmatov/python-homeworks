text = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")

if text.startswith(start_word) and text.endswith(end_word):
    print("Yes, the string starts and ends with the given words.")
else:
    print("No, the string does not match the given start and end words.")
