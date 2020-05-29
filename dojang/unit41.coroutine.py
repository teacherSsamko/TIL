def number_coroutine():
    try:
        while True:  # coroutine을 유지하기 위해 무한 루프 사용
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:
        print()
        print('coroutine close')


co = number_coroutine()
next(co)  # coroutine 함수 안의 yield까지 코드 실행

for i in range(10):
    co.send(i)

co.close()


# def sum_coroutine():
#     total = 0
#     while True:
#         x = (yield total)
#         total += x

def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total


co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))
