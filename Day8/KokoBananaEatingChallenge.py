class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(midValue):
            hours = 0
            for pile in piles:
                hours += (pile + midValue - 1) // midValue
            return hours <= h 

        left , right = 1 , max(piles)

        # Binary search approach
        while left < right:
            mid =  (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1    
        return left        