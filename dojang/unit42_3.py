# 매개변수가 있는 데코레이터
import functools


# def is_multiple(x):
#     def real_decorator(func):
#         def wrapper(a, b):
#             r = func(a, b)
#             if r % x == 0:
#                 print(f'{func.__name__}의 반환값은 {x}의 배수입니다.')
#             else:
#                 print(f'{func.__name__}의 반환값은 {x}의 배수가 아닙니다.')
#             return r
#         return wrapper
#     return real_decorator


# @is_multiple(3)
# def add(a, b):
#     return a + b


# print(add(10, 20))
# print(add(2, 5))

# 매개변수가 있는 데코레이터 여러 개 지정하기


# @is_multiple(3)
# @is_multiple(7)
# def add(a, b):
#     return a + b


# add(10, 20)

# 원래 함수 이름 나오게 하기 functools.wrap 사용


def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print(f'{func.__name__}의 반환값은 {x}의 배수입니다.')
            else:
                print(f'{func.__name__}의 반환값은 {x}의 배수가 아닙니다.')
            return r
        return wrapper
    return real_decorator


@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b


add(10, 20)
