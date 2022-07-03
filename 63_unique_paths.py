class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: [[int]]) -> int:
        if obstacle_grid[0][0] == 1:
            return 0
        else:
            obstacle_grid[0][0] = 1
            
        for i in range(1, len(obstacle_grid[0])):
            if obstacle_grid[0][i] == 1:
                obstacle_grid[0][i] = 0
            else:
                obstacle_grid[0][i] = obstacle_grid[0][i - 1]
                
        for i in range(1, len(obstacle_grid)):
            if obstacle_grid[i][0] == 1:
                obstacle_grid[i][0] = 0
            else:
                obstacle_grid[i][0] = obstacle_grid[i - 1][0]
                
        for i in range(1, len(obstacle_grid)):
            for j in range(1, len(obstacle_grid[0])):
                if obstacle_grid[i][j] == 1:
                    obstacle_grid[i][j] = 0
                else:
                    obstacle_grid[i][j] = obstacle_grid[i - 1][j] + obstacle_grid[i][j - 1]
                    
        return obstacle_grid[len(obstacle_grid) - 1][len(obstacle_grid[0]) - 1]

s = Solution()
print("[[0,0,0],[0,1,0],[0,0,0]]", s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
