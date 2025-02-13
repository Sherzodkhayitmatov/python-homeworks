dic = {"a": 1, "b": {"c": 2}, "d": 3}
has_nested = any(isinstance(v, dict) for v in dic.values())
print(has_nested)
