def text(txt):
    vowels = 'AEIUOaeuio'
    result = ""
    count = 0
    
    for i, char in enumerate(txt):
        result += char
        count += 1
        
        if count == 3:
            if char in vowels:
                if i+1 < len(txt):
                    result += txt[i+1] + '_'
                count = 0
            else:
                result += "_"
                count = 0
    return result 
txt = 'Assalomualaykum'
print(text(txt))