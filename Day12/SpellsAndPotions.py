class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        resArray = []
        for i in range(len(spells)):
            left = 0
            right = len(potions) - 1
            maxCount = 0
            while left <= right:
                mid = (right + left) // 2
                if spells[i] * potions[mid] >= success:
                    maxCount = len(potions) - mid
                    right = mid - 1
                else:
                    left = mid + 1
            resArray.append(maxCount)    
        return resArray            
        