def maximizeGreatness(nums):
    nums.sort()
    count = 0
    j = 0  
    for i in range(len(nums)):
        if nums[j] > nums[i]:
            count += 1
            j += 1
    return count
