class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(index,combinations):
            if index==len(digits):
                output.append(combinations)
                return
            for i in nums[digits[index]]:
                backtrack(index+1,combinations+i)
        output=[]
        backtrack(0,"")
        return output            

