# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def traverse_and_prune(self, node):
        if not node:
            return True
        
        ret_l = self.traverse_and_prune(node.left)
        if ret_l:
            node.left = None
        
        ret_r = self.traverse_and_prune(node.right)
        if ret_r:
            node.right = None
        
        if node.val == 0 and ret_l and ret_r:
            return True
        
        return False
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.traverse_and_prune(root):
            return None
        return root
