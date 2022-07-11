# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_rec(self, x):
        if x:
            l = self.inorder_rec(x.left)
            if self.prev != None and self.prev >= x.val:
                return False
            self.prev = x.val
            return l and self.inorder_rec(x.right)
        else:
            return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.inorder_rec(root)
