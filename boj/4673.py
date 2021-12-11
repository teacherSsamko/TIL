def find_n(n: int, nums: list) -> list:
    str_n = list(map(int, list(str(n))))
    next_n = n + sum(str_n)
    if next_n in nums:
        nums.remove(next_n)
    else:
        return nums

    return find_n(next_n, nums)


all_N = list(range(1, 10001))
self_numbers = []
while all_N:
    n = all_N.pop(0)
    self_numbers.append(n)
    all_N = find_n(n, all_N)

print("\n".join(map(str, self_numbers)))
