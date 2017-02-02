def has22(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 2 and i + 1 < len(nums) and nums[i+1] == 2:
            return True
        i += 1
    return False
