def numMovesStonesII(stones):
    stones.sort()
    n = len(stones)
    
    max_gap = max(stones[i + 1] - stones[i] for i in range(n - 1))
    max_gap = max(max_gap, stones[0] + (stones[-1] - stones[0]) - (n - 1))
    
    min_gap = stones[-1] - stones[0] - (n - 1)
    if min_gap == 0:
        return [0, 0] 
    if min_gap == 1:
        return [1, max_gap]
    return [2, max_gap]
