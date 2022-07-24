# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder_rec(self, x, res):
        if x:
            self.postorder_rec(x.left, res)
            self.postorder_rec(x.right, res)
            res.append(x.val)
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder_rec(root, res)
        return res
