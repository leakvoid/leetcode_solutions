class Solution:
    def pick_first_row(self, matrix, target, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
                    
        if target >= matrix[mid][0] and target <= matrix[mid][-1]:
            if mid == 0:
                return 0
            if target > matrix[mid - 1][-1]:
                return mid
        if target > matrix[mid][-1]:
            return self.pick_first_row(matrix, target, mid + 1, end)
        return self.pick_first_row(matrix, target, start, mid - 1)
    
    def bin_search(self, row, target, start, end):
        if start > end:
            return False
        
        mid = (start + end) // 2
        if target == row[mid]:
            return True
        if target < row[mid]:
            return self.bin_search(row, target, start, mid - 1)
        return self.bin_search(row, target, mid + 1, end)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first = self.pick_first_row(matrix, target, 0, len(matrix) - 1)
        if first == -1:
            return False
        
        for i in range(first, len(matrix)):
            if target < matrix[i][0]:
                return False
            if self.bin_search(matrix[i], target, 0, len(matrix[i]) - 1):
                return True
        return False
