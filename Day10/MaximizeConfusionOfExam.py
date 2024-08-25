class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        TCount=0
        FCount=0
        i=0
        max_len=0
        for j in range(len(answerKey)):
            if answerKey[j] == 'T':
                TCount+=1
            else:
                FCount+=1
            while min(TCount,FCount) > k:
                if answerKey[i] == 'T':
                    TCount -=1 
                else:
                    FCount-=1
                i+=1
            max_len = max(max_len,j-i+1)
        return max_len              

        