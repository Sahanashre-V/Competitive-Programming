from collections import Counter

def maxOperations(nums, k):
    count = Counter(nums)
    pairs = 0
    for num in count:
        complement = k - num
        if complement == num:
            pairs += count[num] // 2 
        elif complement > num:
            pairs += min(count[num], count[complement])
    return pairs
