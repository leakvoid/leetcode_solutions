class Solution:
    def paths_rec(self, m, n, moves_left, row, col):
        if row < 0 or col < 0 or row == m or col == n:
            return 1
        
        if moves_left == 0:
            return 0
        
        if row in self.memory:
            if col in self.memory[row]:
                if moves_left in self.memory[row][col]:
                    return self.memory[row][col][moves_left]
        
        res = 0
        res += self.paths_rec(m, n, moves_left - 1, row + 1, col)
        res += self.paths_rec(m, n, moves_left - 1, row - 1, col)
        res += self.paths_rec(m, n, moves_left - 1, row, col + 1)
        res += self.paths_rec(m, n, moves_left - 1, row, col - 1)
        
        self.memory[row][col][moves_left] = res
        return res
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.memory = {}
        for row in range(m):
            self.memory[row] = {}
            for col in range(n):
                self.memory[row][col] = {}
        
        return self.paths_rec(m, n, maxMove, startRow, startColumn) % (pow(10, 9) + 7)

