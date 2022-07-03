class Solution:
    def replace(self, matrix, row, col):
        for i in range(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = 'z'
                
        for i in range(len(matrix[0])):
            if matrix[row][i] != 0:
                matrix[row][i] = 'z'
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.replace(matrix, i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'z':
                    matrix[i][j] = 0
