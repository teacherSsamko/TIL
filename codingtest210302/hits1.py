def make_smallest(num, k):

    def get_min(result, nums, remain_n):
        if len(nums) <= remain_n or not remain_n:
            return result + nums
        value = min(nums[:remain_n + 1])
        slice_idx = nums.index(value)
        result.append(value)

        return get_min(result, nums[slice_idx + 1:], remain_n - 1)

    remain_n = len(num) - k
    if remain_n == 0:
        return 0

    result = get_min([], list(num), remain_n)

    return int("".join(result))


if __name__ == '__main__':
    num, k = input().split()
    print(make_smallest(num, int(k)))
