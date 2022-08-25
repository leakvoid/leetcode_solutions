class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):
            row = [ matrix[i][0] ]
            for j in range(1, len(matrix[0])):
                row.append( row[j - 1] + matrix[i][j] )
            self.prefix.append(row)

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                self.prefix[i][j] += self.prefix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rb = self.prefix[row2][col2]
        lb = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        ru = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        lu = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return rb - lb - ru + lu

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
