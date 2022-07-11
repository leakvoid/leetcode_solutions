class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generate_rec(self, left, right):
        if left > right:
            return self.empty_node
        
        if right in self.memory[left]:
            return self.memory[left][right]
        
        res = []
        for i in range(left, right + 1):
            left_subtrees = self.generate_rec(left, i - 1)
            right_subtrees = self.generate_rec(i + 1, right)

            for lst in left_subtrees:
                for rst in right_subtrees:
                    res.append( TreeNode(i, lst, rst) )
        
        self.memory[left][right] = res
        return self.memory[left][right]
        
    
    def generateTrees(self, n: int) -> [[TreeNode]]:
        self.empty_node = [None]
        self.memory = {}
        for i in range(n):
            self.memory[i + 1] = {}
        
        return self.generate_rec(1, n)

s = Solution()
for n in range(19):
    res = s.generateTrees(n + 1)
    print(len(res))
