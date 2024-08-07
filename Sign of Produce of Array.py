def arraySign(self, nums: list[int]) -> int:
    prod = 1
    for num in nums:
        if num < 0:
            prod *= -1
        elif num > 0:
            prod *= 1
        else:
            prod *= num
            break
    return prod