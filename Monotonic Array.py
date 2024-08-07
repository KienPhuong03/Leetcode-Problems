def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) <= 2:
            return True
        i = 0
        j = 1
        while True:
            if nums[i] == nums[j]:
                j += 1
                i += 1
                if j > len(nums) - 1:
                    return True
            else:
                break
        if nums[i] < nums[j]:
            while j <= len(nums) - 1:
                if nums[i] <= nums[j]:
                    i += 1
                    j += 1
                else:
                    return False
            return True
        else:
            while j <= len(nums) -1:
                if nums[i] >= nums[j]:
                    i += 1
                    j += 1
                else:
                    return False
            return True