class NQueen:
    def __init__(self, n) -> None:
        self.n = n
    
    def isValidMove(row, col, solution):
        for i in range (0, row):
            old_row = i 
            old_col = solution[i]
            diagonal = row - old_row
            if (old_col == col) or (old_col == col - diagonal) or (old_col == col + diagonal):
                return False
        return True

    
    def findBoardSolutions(self):
        solutionStack = []
        solution  = [-1] * self.n
        result = []
        row = 0
        col = 0

        while row < self.n:
            while col < self.n:
                if NQueen.isValidMove(row, col, solution):
                    solutionStack.append(col)
                    solution[row] = col
                    row += 1
                    col = 0
                    break
                col += 1
            if col == self.n:
                if solutionStack:
                    col = solutionStack.pop() + 1
                    row -= 1
                else:
                    break
            if row == self.n:
                result.append(solution[:])
                row -= 1
                col = solutionStack.pop()+1
        return len(result), result
                
queen = NQueen(1)
len, sol = queen.findBoardSolutions()
print(len, sol)
