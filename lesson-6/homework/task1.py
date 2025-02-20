def zero_check(func):
    def wrapper(*args, **kwarg):
        if any(arg==0 for arg in args):
            raise ValueError("Denominator can't be zero")
        return func(*args, **kwarg)
    return wrapper
@zero_check
def devide(a,b):
    return a/b
print(devide(6,2))