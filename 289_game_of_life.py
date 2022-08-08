DYING_CELL = 2
BORN_CELL = 3

class Solution:
    def get_cell_state(self, board, x, y):
        if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1:
            return 0
        
        if board[x][y] == 1:
            return 1
        if board[x][y] == DYING_CELL:
            return 1
        return 0
    
    def count_neighbors(self, board, x, y):
        count = 0
        count += self.get_cell_state(board, x - 1, y - 1)
        count += self.get_cell_state(board, x - 1, y)
        count += self.get_cell_state(board, x - 1, y + 1)
        count += self.get_cell_state(board, x, y - 1)
        count += self.get_cell_state(board, x, y + 1)
        count += self.get_cell_state(board, x + 1, y - 1)
        count += self.get_cell_state(board, x + 1, y)
        count += self.get_cell_state(board, x + 1, y + 1)
        return count
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                count = self.count_neighbors(board, x, y)
                if board[x][y] == 1:
                    if count < 2 or count > 3:
                        board[x][y] = DYING_CELL
                elif count == 3:
                    board[x][y] = BORN_CELL
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == DYING_CELL:
                    board[x][y] = 0
                elif board[x][y] == BORN_CELL:
                    board[x][y] = 1
