def missingNumber(nums):
    n = len(nums)
    xor_sum = n
    for i in range(n):
        xor_sum ^= i ^ nums[i]
    return xor_sum
