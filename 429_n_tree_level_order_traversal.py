"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def level_traversal(self, stack, res):
        if not stack:
            return
        
        level_vals = []
        new_stack = []
        while stack:
            node = stack.pop()
            level_vals.append( node.val )
            
            for child in node.children:
                new_stack.append( child )
        
        res.append( level_vals )
        
        new_stack.reverse()
        self.level_traversal(new_stack, res)
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        
        res = []
        self.level_traversal([root], res)
        return res
