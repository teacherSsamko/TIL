def type_check(a, b):
    def wrapper(func):
        def inner_wrapper(x, y):
            r = func(x, y)
            if isinstance(x, a) and isinstance(y, b):
                return r
            else:
                raise RuntimeError('자료형이 올바르지 않습니다')
        return inner_wrapper
    return wrapper

@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add('hello', 'world'))