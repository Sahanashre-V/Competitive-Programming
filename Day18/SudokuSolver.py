def solveSudoku(board):
    def isValid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
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
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if isValid(row, col, num):
                            board[row][col] = num  
                            if backtrack():  
                                return True
                            board[row][col] = '.'  
                    return False  
        return True

    backtrack()
