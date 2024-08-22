#Time Limit Exceeded(Leetcode)

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        output=0
        for i in range(len(nums)):
            a=[]
            for j in range(i,len(nums)):
                a.append(nums[j])
                s=max(a) - min(a)
                output+=s
        return output        
