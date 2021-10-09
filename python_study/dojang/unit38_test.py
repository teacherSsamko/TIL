def palindrome(word):
    for i in range(len(word) // 2):
        if not word[i] == word[-1 - i]:
            raise NotPalindromeError
    return print(word)


class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')


try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
