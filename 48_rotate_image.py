class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        half_n = int(n / 2)
        last = n - 1
        for row in range(half_n):
            for col in range(half_n):
                print("1:", row, col, "->", col, last - row)
                matrix[row][col], matrix[col][last - row] = matrix[col][last - row], matrix[row][col]
                
        for row in range(half_n):
            for col in range(half_n):
                print("2:", row, col, "->", last - col, row)
                matrix[row][col], matrix[last - col][row] = matrix[last - col][row], matrix[row][col]

        for row in range(half_n):
            for col in range(half_n):
                print("3:", last - row, col, "->", last - col, last - row)
                matrix[last - row][col], matrix[last - col][last - row] = matrix[last - col][last - row], matrix[last - row][col]

        if n % 2 == 1:
            for row in range(half_n):
                print("e1:", row, half_n, "->", half_n, last - row)
                matrix[row][half_n], matrix[half_n][last - row] = matrix[half_n][last - row], matrix[row][half_n]

            for row in range(half_n):
                print("e2:", row, half_n, "->", half_n, row)
                matrix[row][half_n], matrix[half_n][row] = matrix[half_n][row], matrix[row][half_n]

            for col in range(half_n):
                print("e3:", half_n, last - col, "->", last - col, half_n)
                matrix[half_n][col], matrix[last - col][half_n] = matrix[last - col][half_n], matrix[half_n][col]

s = Solution()
arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(arr)
print("[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]:", arr)
arr = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(arr)
print("[[1,2,3],[4,5,6],[7,8,9]]:", arr)
