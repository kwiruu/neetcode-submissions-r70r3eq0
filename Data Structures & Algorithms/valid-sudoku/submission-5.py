class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkcol = []
        checkrow = []
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                #check if row has no duplicate
                if board[i][j] == ".":
                    continue
                if board[i][j] not in checkrow:
                    checkrow.append(board[i][j])
                    continue
                else:
                    return False
            checkrow = []

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                #check if col has no duplicate
                if board[j][i] == ".":
                    continue
                if board[j][i] not in checkcol:
                    checkcol.append(board[j][i])
                    continue
                else:
                    return False
            checkcol = []

        for square in range(9):
            checksquare = []
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] not in checksquare:
                        checksquare.append(board[row][col])
                        continue
                    else:
                        return False
                    

        return True