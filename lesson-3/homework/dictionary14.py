dic = {
    "key": "new",
    "key2": "new2",
    "key3": "new3",
    "key4": "new2"
}
val = 'new2'
result = [k for k in dic if dic[k] == val]
print(result)

