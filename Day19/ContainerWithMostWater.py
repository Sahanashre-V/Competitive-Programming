def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
