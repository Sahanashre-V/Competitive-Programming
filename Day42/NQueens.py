def solveNQueens(n):
    def backtrack(row, cols, diag1, diag2, board, solutions):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1, cols, diag1, diag2, board, solutions)
            
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    solutions = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board, solutions)
    return solutions
