class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index,subsets):
            output.append(subsets)
            for i in range(index,len(nums)):
                backtrack(i+1,subsets+[nums[i]])
        output=[]
        backtrack(0,[])
        return output        
    