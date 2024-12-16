def maximizeGreatness(nums):
    nums.sort() 
    greatness = 0
    j = 0  
    
    for num in nums:
        while j < len(nums) and nums[j] <= num:
            j += 1
        if j < len(nums):  
            greatness += 1
            j += 1  

    return greatness
