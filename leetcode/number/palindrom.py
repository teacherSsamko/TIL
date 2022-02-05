def isPalindrome(x: int) -> bool:
    tmp = x
    reversed_num = 0

    while tmp > 0:
        last_digit = tmp % 10
        reversed_num = reversed_num * 10 + last_digit
        tmp //= 10

    return reversed_num == x


if __name__ == "__main__":
    print(isPalindrome(1321))
