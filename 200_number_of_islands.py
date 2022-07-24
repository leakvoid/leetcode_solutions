class Solution:
    def find_island(self, grid, row, col):
        grid[row][col] = '0'
        
        if row + 1 < len(grid) and grid[row + 1][col] == '1':
            self.find_island(grid, row + 1, col)
        if row > 0 and grid[row - 1][col] == '1':
            self.find_island(grid, row - 1, col)
        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
            self.find_island(grid, row, col + 1)
        if col > 0 and grid[row][col - 1] == '1':
            self.find_island(grid, row, col - 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.find_island(grid, row, col)
                    res += 1
                    
        return res
