# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_rec(self, x, depth):
        if x:
            depth += 1
            if depth > self.max_depth:
                self.max_depth = depth
            
            self.traverse_rec(x.left, depth)
            self.traverse_rec(x.right, depth)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.traverse_rec(root, 0)
        return self.max_depth
