text = input("Enter the text: ")


vowels = 'aeiouAEIOU'
vowel_count = 0


for char in text:
    if char in vowels:
        vowel_count += 1

char_lenth = len(text)
consonant = char_lenth - vowel_count

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant}")
    
