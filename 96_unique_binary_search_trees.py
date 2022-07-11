class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def unique_bst_count(self, left, right):
        if left >= right:
            return 1
        
        if right in self.memory[left]:
            return self.memory[left][right]
        
        total_count = 0
        for i in range(left, right + 1):
            total_count += self.unique_bst_count(left, i - 1) * self.unique_bst_count(i + 1, right)

        self.memory[left][right] = total_count
        return total_count
    
    def numTrees(self, n: int) -> int:
        self.memory = {}
        for i in range(n):
            self.memory[i + 1] = {}
        
        return self.unique_bst_count(1, n)

s = Solution()
for i in range(19):
    print(s.numTrees(i + 1))
