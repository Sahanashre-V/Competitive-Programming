class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        whole = sum(nums)
        
        if whole % 2 != 0:
            return False
        
        target = whole // 2

        def combination(index, total):
            if total == target:
                return True
            if total > target or index>=len(nums):
                return False
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                if combination(i + 1, total + nums[i]):
                    return True
            return False
        
        return combination(0,0)