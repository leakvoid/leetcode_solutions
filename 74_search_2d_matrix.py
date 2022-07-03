class Solution:
    def find_col(self, row, target, start, end):
        if start > end:
            return False
        
        mid = start + (end - start) // 2
        if target == row[mid]:
            return True
        elif target > row[mid]:
            return self.find_col(row, target, mid + 1, end)
        else:
            return self.find_col(row, target, start, mid - 1)
            
        
    
    def find_row(self, matrix, target, start, end):
        if start > end:
            return False
        
        mid = start + (end - start) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][-1]:
            return self.find_col(matrix[mid], target, 0, len(matrix[mid]) - 1)
        elif target > matrix[mid][0]:
            return self.find_row(matrix, target, mid + 1, end)
        else:
            return self.find_row(matrix, target, start, mid - 1)
    
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        return self.find_row(matrix, target, 0, len(matrix) - 1)

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
