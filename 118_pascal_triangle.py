class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            pascal.append( (i + 1) * [1] )
            
        for i in range(2, len(pascal)):
            for j in range(1, len(pascal[i]) - 1):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal
