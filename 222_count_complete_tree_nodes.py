# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightmost_empty(self, node, depth):
        if depth == self.tree_depth:
            return (node == None)
        
        return self.rightmost_empty(node.right, depth + 1)
        
    def tree_binary_search(self, node, depth):
        if depth == self.tree_depth:
            if node:
                self.last_level_nodes += 1
            return
        
        if self.rightmost_empty(node.left, depth + 1):
            self.tree_binary_search(node.left, depth + 1)
        else:
            self.last_level_nodes += pow(2, self.tree_depth - depth - 1)
            self.tree_binary_search(node.right, depth + 1)
            
    def get_tree_depth(self, node):
        if node:
            return 1 + self.get_tree_depth(node.left)
        else:
            return -1
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.tree_depth = self.get_tree_depth(root)
        if self.tree_depth == -1:
            return 0
        if self.tree_depth == 0:
            return 1
        
        self.last_level_nodes = 0
        self.tree_binary_search(root, 0)
        return pow(2, self.tree_depth) - 1 + self.last_level_nodes
