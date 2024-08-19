import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) < 3:
            return
        resultSum = nums[0] + nums[1] + nums[2]
        min_difference = sys.maxsize
        for i in range(0,len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                totalSum = nums[i] + nums[left] + nums[right]
                if totalSum == target:
                    return target
                elif totalSum < target:
                    left+=1
                else:
                    right-=1        
                diff = abs(target - totalSum)
                if diff < min_difference:
                    min_difference = diff
                    resultSum = totalSum
        return resultSum            

 