def solveNQueens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(["." * i + "Q" + "." * (n - i - 1) for i in board])
            return
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col  
                backtrack(board, row + 1)  
                board[row] = -1  

    result = []
    backtrack([-1] * n, 0) 
    return result
