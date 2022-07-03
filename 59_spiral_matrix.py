class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        matrix = [''] * n
        for i in range(n):
            matrix[i] = [''] * n
        
        left_bound = 0
        right_bound = n - 1
        upper_bound = 0
        lower_bound = n - 1
        
        num = 1
        while num <= n * n:
            for i in range(left_bound, right_bound + 1):
                matrix[upper_bound][i] = num
                num += 1
            upper_bound += 1
            if upper_bound > lower_bound:
                return matrix
            
            for i in range(upper_bound, lower_bound + 1):
                matrix[i][right_bound] = num
                num += 1
            right_bound -= 1
            if left_bound > right_bound:
                return matrix
            
            for i in range(right_bound, left_bound - 1, -1):
                matrix[lower_bound][i] = num
                num += 1
            lower_bound -= 1
            if upper_bound > lower_bound:
                return matrix
            
            for i in range(lower_bound, upper_bound - 1, -1):
                matrix[i][left_bound] = num
                num += 1
            left_bound += 1
            if left_bound > right_bound:
                return matrix
        
        return matrix

s = Solution()
print("3", s.generateMatrix(3))
