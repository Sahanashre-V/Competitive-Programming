def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    
    curr_end = float('-inf')  
    max_length = 0
    
    for pair in pairs:
        if pair[0] > curr_end:
            curr_end = pair[1]  
            max_length += 1
    
    return max_length
