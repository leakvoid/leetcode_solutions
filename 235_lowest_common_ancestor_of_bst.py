# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_least_common_ancestor(self, node, p, q):
        self.lca = node
        
        if p.val < node.val and q.val < node.val:
            self.find_least_common_ancestor(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            self.find_least_common_ancestor(node.right, p, q)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find_least_common_ancestor(root, p, q)
        return self.lca
