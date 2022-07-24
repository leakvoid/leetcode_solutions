class Solution:
    def mark_connected_regions(self, board, row, col, edge_connections):
        if edge_connections[row][col] == 1:
            return
        
        edge_connections[row][col] = 1
        if (row + 1) < len(board) and board[row + 1][col] == 'O':
            self.mark_connected_regions(board, row + 1, col, edge_connections)
        if row > 0 and board[row - 1][col] == 'O':
            self.mark_connected_regions(board, row - 1, col, edge_connections)
        if (col + 1) < len(board[0]) and board[row][col + 1] == 'O':
            self.mark_connected_regions(board, row, col + 1, edge_connections)
        if col > 0 and board[row][col - 1] == 'O':
            self.mark_connected_regions(board, row, col - 1, edge_connections)
    
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        edge_connections = []
        for r in range(len(board)):
            edge_connections.append([0] * len(board[0]))
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.mark_connected_regions(board, i, 0, edge_connections)
            if board[i][-1] == 'O':
                self.mark_connected_regions(board, i, len(board[0]) - 1, edge_connections)
        
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.mark_connected_regions(board, 0, i, edge_connections)
            if board[-1][i] == 'O':
                self.mark_connected_regions(board, len(board) - 1, i, edge_connections)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and edge_connections[row][col] == 0:
                    board[row][col] = 'X'
        return board

s = Solution()
print('[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]:', s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
