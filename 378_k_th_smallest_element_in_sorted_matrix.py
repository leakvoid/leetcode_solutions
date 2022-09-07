import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        h = []
        for row in range(n):
            heapq.heappush(h, (matrix[row][0], row, 0))
        
        for i in range(k):
            (val, row, col) = heapq.heappop(h)
            col += 1
            if col < len(matrix):
                heapq.heappush(h, (matrix[row][col], row, col))
        
        return val
