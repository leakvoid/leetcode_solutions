class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [None] * m
        for i in range(m):
            matrix[i] = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]

s = Solution()
