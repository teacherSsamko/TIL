def trace(func):
    def wrapper(a, b):
        r = func(a, b)
        print(f'{func.__name__}(a={a}, b={b}) -> {r}')
        return r
    return wrapper


@trace
def add(a, b):
    return a + b


@trace
def multiply(a, b):
    return a * b


print(add(10, 20))
print(multiply(10, 3))
