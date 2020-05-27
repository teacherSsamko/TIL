# def three_multiple():
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아니잖아요!')
#     print(x)


# try:
#     three_multiple()
# except Exception as e:
#     print('Error raised.', e)


class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


def three_multiple():
    try:
        x = int(input('put 3 multiple number: '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('Exception Error raised.', e)


three_multiple()
