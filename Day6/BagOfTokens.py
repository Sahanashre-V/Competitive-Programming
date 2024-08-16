class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left=0
        right=len(tokens)-1
        score=0
        while left<=right:
            if power>=tokens[left]:
                power-=tokens[left]
                left+=1
                score+=1
            else:
                if power+tokens[right]>=tokens[left] and right!=left and score!=0:
                    power+=tokens[right]
                    right-=1
                    score-=1
                else:
                    break
        return score                 