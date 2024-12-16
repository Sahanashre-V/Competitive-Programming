def findUnsortedSubarray(arr):
    n = len(arr)
    left, right = -1, -1
    
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            left = i - 1
            break
    
    if left == -1:
        return 0
    
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right = i + 1
            break
    
    subarray_min = min(arr[left:right+1])
    subarray_max = max(arr[left:right+1])
    
    while left >= 0 and arr[left] > subarray_min:
        left -= 1
    
    while right < n and arr[right] < subarray_max:
        right += 1
    
    return right - left - 1
