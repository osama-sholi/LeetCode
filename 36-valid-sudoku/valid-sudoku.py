class Solution(object):
    def isValidSudoku(self, board):
        def find_square(row, column):
            index = 0
            for i in range(row + 1):
                index += 3
            for j in range(column + 1):
                index += 1
        square_set = {}
        column_set = {}
        for i in range(9):
            square_set[i] = set()
            column_set[i] = set()
        
        # validate rows and squres
        for i in range(9):
            row_set = set()
            for j in range(9):
                print(i,j)
                val = board[i][j]
                if val == '.':
                    continue

                if val in row_set:
                    print(row_set)
                    return False
                else:
                    row_set.add(val)

                if val in column_set[j]:
                    print(column_set)
                    return False
                else:
                    column_set[j].add(val)

                square = i/3*3 + j/3
                print(square)
                if val in square_set[square]:
                    print(square_set)
                    return False
                else:
                    square_set[square].add(val)

        return True                