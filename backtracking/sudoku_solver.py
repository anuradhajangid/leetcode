DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    
def solve_sudoku(board):
    # Replace this placeholder return statement with your code
    row,col = 0,0
    dfs(board, row, col)
    return board

def dfs(grid, row, col):
    if (row == 9 - 1 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] in DIGITS:
        return dfs(grid, row, col + 1)
    for num in DIGITS: 
        if isValid(grid, num, row, col):
            grid[row][col] = num
            if dfs(grid, row, col + 1):
                return True
        grid[row][col] = "."
    return False

def isValid(board, digit, row, col):
    for i in range(0,9):
        if board[row][i] == digit:
            return False
        if board[i][col] == digit:
            return False
    rs,cs= 0,0
    rs = 3*int(row/3)
    cs = 3*int(col/3)
    if digit in [board[rs][cs], board[rs][cs+1], board[rs][cs+2], board[rs+1][cs], board[rs+1][cs+1], board[rs+1][cs+2], board[rs+2][cs], board[rs+2][cs+1], board[rs+2][cs+2]]:
        return False
    return True

        



# driver code
def main():
    sudokus = [[[".",".",".",".",".",".",".","7","."],["2","7","5",".",".",".","3","1","4"],[".",".",".",".","2","7",".","5","."],["9","8",".",".",".",".",".","3","1"],[".","3","1","8",".","4",".",".","."],[".",".",".","1",".",".","8",".","5"],["7",".","6","2",".",".","1","8","."],[".","9",".","7",".",".",".",".","."],["4","1",".",".",".","5",".",".","7"]],
               [[".",".","6",".",".","4",".",".","."],[".","3",".",".","1",".",".","9","5"],[".",".",".",".",".",".","8",".","."],[".",".",".",".","8",".","3",".","."],["4",".",".",".",".","1",".","8","2"],[".","2",".",".",".",".","7",".","."],[".",".",".",".",".",".",".",".","7"],[".","5",".",".","9",".",".","2","1"],["3",".",".","5",".",".",".",".","."]],
               [["6",".",".",".",".",".","1",".","."],[".",".",".","3",".",".",".",".","."],[".","9",".",".","4","7",".","8","."],["9",".",".",".","5","3",".",".","6"],[".",".",".","2",".",".",".","5","."],[".","3",".","8",".",".",".",".","."],[".","7",".",".","9","5",".","4","."],[".",".","4",".",".",".",".",".","8"],[".",".",".",".","2",".",".",".","."]],
               [[".",".",".",".",".",".","7",".","."],[".","4",".",".","3",".",".","6","5"],[".",".","1",".",".","8",".",".","."],[".","6",".",".","5",".",".","3","9"],["4",".",".","6",".",".",".",".","."],[".",".",".",".",".",".",".","2","."],["8",".",".",".",".","3",".","9","7"],[".",".",".",".","7",".","4",".","."],[".","9",".",".",".",".","2",".","."]],
               [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]]

    for sudoku in sudokus:
        print(f"Input Sudoku: {sudoku}")
        print(f"Output: {solve_sudoku(sudoku)}")
        print("-" * 100)


if __name__ == '__main__':
    main()