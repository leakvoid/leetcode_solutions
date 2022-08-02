# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

NONE_FOUND = 0
P_FOUND = 1
Q_FOUND = 2
BOTH_FOUND = 3

class Solution:
    def find_lowest_common_ancestor(self, node, p, q):
        if not node:
            return NONE_FOUND
        
        res1 = self.find_lowest_common_ancestor(node.left, p, q)
        if res1 == BOTH_FOUND:
            return res1
        res2 = self.find_lowest_common_ancestor(node.right, p, q)
        if res2 == BOTH_FOUND:
            return res2
        
        cur_status = NONE_FOUND
        if node == p:
            cur_status = P_FOUND
        elif node == q:
            cur_status = Q_FOUND
            
        res = cur_status | res1 | res2
        if res == BOTH_FOUND:
            self.lca = node
        return res
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find_lowest_common_ancestor(root, p, q)
        return self.lca
