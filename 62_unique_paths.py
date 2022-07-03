class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [None] * m
        for i in range(m):
            matrix[i] = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]

    # [1, 1, 1, 1, 1, 1, 1],
    # [1, 2, 3, 4, 5, 6, 7],
    # [1, 3, 6,10,15,21,28]

s = Solution()
print("3*7:", s.uniquePaths(3, 7))
print("3*2:", s.uniquePaths(3, 2))
