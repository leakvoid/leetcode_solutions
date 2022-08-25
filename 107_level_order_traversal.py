# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        unrolled = []
        
        level = [root]
        while level:
            unrolled.append(level)
            prev_level = level
            level = []
            
            for i in range( len(prev_level) ):
                if prev_level[i].left:
                    level.append(prev_level[i].left)
                if prev_level[i].right:
                    level.append(prev_level[i].right)

        res = []
        for i in range(len(unrolled) - 1, -1, -1):
            r = []
            for n in unrolled[i]:
                r.append(n.val)
            res.append(r)
        
        return res
