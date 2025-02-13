from collections import defaultdict

dic = defaultdict(lambda: "Not Found")
dic["a"] = 1

print(dic["a"])
print(dic["b"]) 
