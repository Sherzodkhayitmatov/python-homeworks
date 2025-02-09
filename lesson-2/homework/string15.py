text = input("Enter a sentence: ")

acronym = "".join(word[0].upper() for word in text.split())

print("Acronym:", acronym)
