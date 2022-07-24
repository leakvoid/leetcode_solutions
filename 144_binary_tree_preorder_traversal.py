# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_rec(self, x, res):
        if x:
            res.append(x.val)
            self.preorder_rec(x.left, res)
            self.preorder_rec(x.right, res)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorder_rec(root, res)
        return res
