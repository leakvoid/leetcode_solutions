class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        upper_b = 0
        lower_b = len(matrix) - 1
        left_b = 0
        right_b = len(matrix[0]) - 1
        matrix_size = len(matrix) * len(matrix[0])
        
        res = []
        while True:
            # top: left to right
            for i in range(left_b, right_b + 1):
                res.append(matrix[upper_b][i])
            upper_b += 1
            if upper_b > lower_b:
                return res
            
            # right: up to bottom
            for i in range(upper_b, lower_b + 1):
                res.append(matrix[i][right_b])
            right_b -= 1
            if left_b > right_b:
                return res
            
            # bottom: right to left
            for i in range(right_b, left_b - 1, -1):
                res.append(matrix[lower_b][i])
            lower_b -= 1
            if upper_b > lower_b:
                return res
            
            # left: bottom to up
            for i in range(lower_b, upper_b - 1, -1):
                res.append(matrix[i][left_b])
            left_b += 1
            if left_b > right_b:
                return res

s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
