class Solution:
    def min_path_rec(self, triangle, depth, idx):
        if depth == len(triangle) - 1:
            return triangle[depth][idx]
        
        if idx in self.memory[depth]:
            return self.memory[depth][idx]
        
        self.memory[depth][idx] = triangle[depth][idx] + min(self.min_path_rec(triangle, depth + 1, idx), self.min_path_rec(triangle, depth + 1, idx + 1))
        return self.memory[depth][idx]
    
    def minimumTotal_memorization(self, triangle: List[List[int]]) -> int:
        self.memory = []
        for depth in range(len(triangle)):
            self.memory.append({})
        
        return self.min_path_rec(triangle, 0, 0)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
