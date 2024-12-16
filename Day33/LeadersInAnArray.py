def leaders(arr):
    n = len(arr)
    leaders_list = []
    max_right = arr[-1]
    leaders_list.append(max_right)  
    
    for i in range(n-2, -1, -1):  
        if arr[i] >= max_right:
            leaders_list.append(arr[i])
            max_right = arr[i]
    
    return leaders_list[::-1]  
