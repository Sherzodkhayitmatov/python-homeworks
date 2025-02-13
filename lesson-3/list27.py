def max_sublist(lst, start, end):
    sublist = lst[start:end+1]
    return max(sublist)
print(max_sublist)