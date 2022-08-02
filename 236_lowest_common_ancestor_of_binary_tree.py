# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_node_path(self, node, target):
        if node:
            if node == target:
                return [node]
            
            res = self.get_node_path(node.left, target)
            if res:
                res.append(node)
                return res
            
            res = self.get_node_path(node.right, target)
            if res:
                res.append(node)
                return res
        return None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.get_node_path(root, p)
        q_path = self.get_node_path(root, q)
        
        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[len(p_path) - i - 1] != q_path[len(q_path) - i - 1]:
                return p_path[len(p_path) - i]
            i += 1
            
        if i == len(p_path):
            return p_path[0]
        return q_path[0]
