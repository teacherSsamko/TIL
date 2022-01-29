def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    x = str(x)
    if x == x[::-1]:
        return True
    return False


if __name__ == "__main__":
    print(isPalindrome(1221))
