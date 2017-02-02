def centered_average(nums):
    sum = 0
    for i in nums:
        sum += i
    sum = sum - max(nums) - min(nums)
    return sum / (len(nums) - 2)
