# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_rec(self, x, level, res):
        if x:
            if level == len(res):
                res.append([])
            if level % 2:
                res[level].insert(0, x.val)
            else:
                res[level].append(x.val)
            
            self.traverse_rec(x.left, level + 1, res)
            self.traverse_rec(x.right, level + 1, res)
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.traverse_rec(root, 0, res)
        return res
