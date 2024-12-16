def secondLargest(arr):
    if len(arr) < 2:
        return None  
    
    first, second = float('-inf'), float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None  
