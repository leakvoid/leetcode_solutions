# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_rec(self, node):
        if node:
            self.inorder_rec(node.left)
            self.count += 1
            if self.count == self.target:
                self.res = node.val
                return
            self.inorder_rec(node.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.target = k
        self.count = 0
        self.res = None
        self.inorder_rec(root)
        return self.res
