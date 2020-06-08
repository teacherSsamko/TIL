# 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기
class Trace:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        print(f'{self.func.__name__}(args={args}, kwargs={kwargs}) -> {r}')

        return r


# @Trace
# def add(a, b):
#     return a + b


print(add(10, 20))
print(add(a=19, b=20))

# 클래스로 매개변수가 있는 데코레이터 만들기


class IsMultiple:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print(f'{func.__name__}의 반한값은 {self.x}의 배수입니다.')
            else:
                print(f'{func.__name__}의 반한값은 {self.x}의 배수가 아닙니다.')

            return r
        return wrapper


@IsMultiple(3)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))
