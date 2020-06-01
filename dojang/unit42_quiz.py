def type_check(a, b):
    def wrapper(func):
        def inner_wrapper(x, y):
            r = func(x, y)
            if type(x) == a and type(y) == b:
                return r
            else:
                raise RuntimeError('자료형이 올바르지 않습니다')

@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add('hello', 'world'))