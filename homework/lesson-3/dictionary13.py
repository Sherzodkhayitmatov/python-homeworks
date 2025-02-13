dic = {
    "key": "new",
    "key2": "new2",
    "key3": "new3",
    "key4": "new2"
}
swapped_dic = {value: key for key, value in dic.items()}

print(swapped_dic)
