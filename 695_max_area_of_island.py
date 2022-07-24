class Solution:
    def pass_island(self, row, col, grid,  explo_grid):
        if explo_grid[row][col] == 1:
            return 0
        explo_grid[row][col] = 1
        
        area = 1
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            area += self.pass_island(row + 1, col, grid, explo_grid)
        if row > 0 and grid[row - 1][col] == 1:
            area += self.pass_island(row - 1, col, grid, explo_grid)
        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
            area += self.pass_island(row, col + 1, grid, explo_grid)
        if col > 0 and grid[row][col - 1] == 1:
            area += self.pass_island(row, col - 1, grid, explo_grid)
        return area
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        explo_grid = []
        for r in range(len(grid)):
            explo_grid.append([0] * len(grid[0]))
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.pass_island(row, col, grid, explo_grid)
                    if area > max_area:
                        max_area = area
                        
        return max_area
