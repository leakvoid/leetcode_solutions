# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_rec(self, x, y):
        if x and y:
            if x.val != y.val:
                return False
            return self.traverse_rec(x.left, y.right) and self.traverse_rec(x.right, y.left)
        elif not x and not y:
            return True
        else:
            return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse_rec(root.left, root.right)
