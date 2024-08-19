class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0 
        left , right = 0 , len(height)-1   
        max_left , max_right = height[left] , height[right]
        trapped_water = 0
        while left < right:
            if height[left] <= height[right]:
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    trapped_water += max_left - height[left]
                left+=1    
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    trapped_water += max_right - height[right]
                right-=1    
        return trapped_water                        
