class Solution(object):
    def isValidSudoku(self, board):
        square_set = {}
        column_set = {}
        for i in range(9):
            square_set[i] = set()
            column_set[i] = set()
        
        for i in range(9):
            row_set = set()
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                if val in row_set:
                    return False
                else:
                    row_set.add(val)

                if val in column_set[j]:
                    return False
                else:
                    column_set[j].add(val)

                square = i/3*3 + j/3
                if val in square_set[square]:
                    return False
                else:
                    square_set[square].add(val)

        return True                