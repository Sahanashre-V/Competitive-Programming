def count_subarrays_with_max_less_than_or_equal_to(nums, x):
    count = 0
    length = 0
    for num in nums:
        if num <= x:
            length += 1
            count += length
        else:
            length = 0
    return count

def numSubarrayBoundedMax(nums, left, right):
    return count_subarrays_with_max_less_than_or_equal_to(nums, right) - count_subarrays_with_max_less_than_or_equal_to(nums, left - 1)
