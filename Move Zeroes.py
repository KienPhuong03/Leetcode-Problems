
### TOO SLOW! only faster than 5%
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            print(f"found a zero at index {i}")
            j = i
            while j < len(nums)-1 and nums[j] == 0:
                j += 1
                print(f"j is now at {j}")
            print(f"about to swap elements at index {i} and {j}, which are {nums[i]} and {nums[j]}")
            nums[i], nums[j] = nums[j], nums[i]
            print(f'nums is now {nums} after swap')
            i += 1
        else:
            i += 1

sample = [0,1,0,3,12]
moveZeroes(sample)
print(sample)


### Faster
def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 1
    while j <= len(nums) - 1:
        if nums[i] == 0:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        else:
            i += 1
            j += 1