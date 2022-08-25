# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_rec(self, node, level, res):
        if node:
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            self.traverse_rec(node.left, level + 1, res)
            self.traverse_rec(node.right, level + 1, res)
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.traverse_rec(root, 0, res)
        return reversed(res)
