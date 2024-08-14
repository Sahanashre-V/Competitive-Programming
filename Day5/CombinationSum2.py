class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index,combination,total):
            if total == target:
                output.append(combination)
                return
            if total > target:
                return  
            for i in range(index,len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1,combination+[candidates[i]],total+candidates[i])  
        candidates.sort()       
        output=[]
        backtrack(0,[],0)
        return output     
