# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inverse_rec(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.inverse_rec(node.left)
            self.inverse_rec(node.right)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inverse_rec(root)
        return root
