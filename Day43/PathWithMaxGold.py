def getMaximumGold(grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(x, y, gold_collected):
        if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0:
            return gold_collected
        
        current_gold = grid[x][y]
        grid[x][y] = 0  
        
        max_gold = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            max_gold = max(max_gold, dfs(x + dx, y + dy, gold_collected + current_gold))
        
        grid[x][y] = current_gold 
        return max_gold
    
    max_gold_collected = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 0:
                max_gold_collected = max(max_gold_collected, dfs(i, j, 0))
    
    return max_gold_collected
