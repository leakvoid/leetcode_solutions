# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_rec(self, node):
        if not node:
            return ""
        
        res = str(node.val)
        res_l = self.traverse_rec(node.left)
        res_r = self.traverse_rec(node.right)
        
        if res_l:
            res += '(' + res_l + ')'
            if res_r:
                res += '(' + res_r + ')'
        elif res_r:
            res += '()(' + res_r + ')'
        
        return res
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse_rec(root)
