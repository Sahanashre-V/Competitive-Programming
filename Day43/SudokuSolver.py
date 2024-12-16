def solveSudoku(board):
    def isValid(board, row, col, num):
        num = str(num)
        if num in board[row]:
            return False
        for i in range(9):
            if board[i][col] == num:
                return False
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in range(1, 10):
                        if isValid(board, row, col, num):
                            board[row][col] = str(num)
                            if backtrack():
                                return True
                            board[row][col] = "."  
                    return False
        return True

    backtrack()
