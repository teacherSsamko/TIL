def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    x = str(x)
    mid = len(x) // 2
    if len(x) % 2:
        if x[: mid + 1] == x[mid:][::-1]:
            return True
    else:
        if x[:mid] == x[mid:][::-1]:
            return True
    return False


if __name__ == "__main__":
    print(isPalindrome(1221))
