class Solution:
    def dfs(self, row, col, grid, visited):
        visited[row][col] = True

        if row + 1 == len(grid) or grid[row + 1][col] == 0:
            self.perimeter += 1
        elif not visited[row + 1][col]:
            self.dfs(row + 1, col, grid, visited)
        
        if row - 1 < 0 or grid[row - 1][col] == 0:
            self.perimeter += 1
        elif not visited[row - 1][col]:
            self.dfs(row - 1, col, grid, visited)
        
        if col + 1 == len(grid[0]) or grid[row][col + 1] == 0:
            self.perimeter += 1
        elif not visited[row][col + 1]:
            self.dfs(row, col + 1, grid, visited)
        
        if col - 1 < 0 or grid[row][col - 1] == 0:
            self.perimeter += 1
        elif not visited[row][col - 1]:
            self.dfs(row, col - 1, grid, visited)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = []
        for i in range(len(grid)):
            visited.append([False] * len(grid[0]))
        
        self.perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid, visited)
                    return self.perimeter
