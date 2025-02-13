dic = {"a": 1, "b": 2, "c": 1, "d": 3}
sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
 
print(sorted_dic)
