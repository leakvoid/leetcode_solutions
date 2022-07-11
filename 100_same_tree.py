# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_rec(self, x, y):
        if x and y:
            if x.val != y.val:
                return False
            return self.inorder_rec(x.left, y.left) and self.inorder_rec(x.right, y.right)
        elif not x and not y:
            return True
        else:
            return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorder_rec(p, q)
