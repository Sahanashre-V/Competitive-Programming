def maxAtIndex(arr, index, bound):
    left = max(0, index - bound)
    right = min(len(arr) - 1, index + bound)

    max_value = max(arr[left:right+1])

    return max_value
