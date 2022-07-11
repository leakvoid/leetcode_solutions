# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_rec(self, x, res):
        if x:
            self.inorder_rec(x.left, res)
            if self.prev != None and self.prev.val >= x.val:
                res.append(self.prev)
                res.append(x)
            self.prev = x
            self.inorder_rec(x.right, res)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.prev = None
        self.inorder_rec(root, res)
        if len(res) == 2:
            res[0].val, res[1].val = res[1].val, res[0].val
        else:
            res[0].val, res[3].val = res[3].val, res[0].val
