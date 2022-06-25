from copy import deepcopy

class Solution:
    def exhaust_by_row(self, guess, row, col, board):
        for i in range(9):
            cell = board[row][i]
            if cell != "." and cell in guess:
                guess.remove(cell)
        
    def exhaust_by_column(self, guess, row, col, board):
        for i in range(9):
            cell = board[i][col]
            if cell != "." and cell in guess:
                guess.remove(cell)
        
    def exhaust_by_square(self, guess, row, col, board):
        row_start = row - row % 3
        col_start = col - col % 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                cell = board[i][j]
                if cell != "." and cell in guess:
                    guess.remove(cell)
    
    def build_estimates(self, board):
        guess_table = {}
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    guess = ["1","2","3","4","5","6","7","8","9"]
                    self.exhaust_by_row(guess, i, j, board)
                    self.exhaust_by_column(guess, i, j, board)
                    self.exhaust_by_square(guess, i, j, board)

                    if i in guess_table:
                        guess_table[i][j] = guess
                    else:
                        guess_table[i] = {}
                        guess_table[i][j] = guess

        return guess_table

    def remove_by_row(self, guess_table, row, val):
        for j in guess_table[row]:
            guess = guess_table[row][j]
            if val in guess:
                guess.remove(val)
    
    def remove_by_column(self, guess_table, col, val):
        for i in guess_table:
            if col in guess_table[i]:
                guess = guess_table[i][col]
                if val in guess:
                    guess.remove(val)

    def remove_by_square(self, guess_table, row, col, val):
        row_start = row - row % 3
        col_start = col - col % 3
        for i in range(row_start, row_start + 3):
            if i in guess_table:
                for j in range(col_start, col_start + 3):
                    if j in guess_table[i]:
                        guess = guess_table[i][j]
                        if val in guess:
                            guess.remove(val)
    
    def resolve_simple_cases(self, board, guess_table):
        node_removed = True
        while node_removed:
            node_removed = False
            to_be_removed = []
            for i in guess_table:
                for j in guess_table[i]:
                    guess = guess_table[i][j]
                    if len(guess) == 1:
                        node_removed = True
                        board[i][j] = guess[0]
                        to_be_removed.append([i, j])

                        self.remove_by_row(guess_table, i, board[i][j])
                        self.remove_by_column(guess_table, j, board[i][j])
                        self.remove_by_square(guess_table, i, j, board[i][j])

            for r in to_be_removed:
                row = r[0]
                col = r[1]
                guess_table[row].pop(col, None)
                if len(guess_table[row]) == 0:
                    guess_table.pop(row, None)

        for i in guess_table:
            for j in guess_table[i]:
                guess = guess_table[i][j]
                if len(guess) == 0:
                    return False

        return True

    def take_smallest_guess(self, guess_table):
        min_len = 10
        min_i = 0
        min_j = 0
        for i in guess_table:
            for j in guess_table[i]:
                g_len = len(guess_table[i][j])
                if g_len == 2:
                    return (i, j)
                if g_len < min_len:
                    min_len = g_len
                    min_i = i
                    min_j = j
        return (min_i, min_j)

    def solve_with_backtracking(self, board, guess_table):        
        if self.resolve_simple_cases(board, guess_table):
            if len(guess_table) == 0:
                return (True, board)
            else:
                (i, j) = self.take_smallest_guess(guess_table)
                guess = guess_table[i][j]

                guess_table[i].pop(j, None)
                if len(guess_table[i]) == 0:
                    guess_table.pop(i, None)

                for k in guess:
                    new_board = deepcopy(board)
                    new_board[i][j] = k
                    new_guess_table = deepcopy(guess_table)
                    self.remove_by_row(new_guess_table, i, new_board[i][j])
                    self.remove_by_column(new_guess_table, j, new_board[i][j])
                    self.remove_by_square(new_guess_table, i, j, new_board[i][j])

                    (flag, new_board) = self.solve_with_backtracking(new_board, new_guess_table)
                    if flag:
                        return (True, new_board)
        return (False, board)
    
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        guess_table = self.build_estimates(board)
        (flag, new_board) = self.solve_with_backtracking(board, guess_table)
        for i in range(9):
            for j in range(9):
                board[i][j] = new_board[i][j]

s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print('\n board solution')
for row in board:
    print('\n', row)
    
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
s.solveSudoku(board)
print('\n board solution')
for row in board:
    print('\n', row)
