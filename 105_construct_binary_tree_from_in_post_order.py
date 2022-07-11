# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_tree(self, preorder, inorder, left, right):
        if self.preorder_pos == len(preorder):
            return None
        
        val = preorder[self.preorder_pos]
        split = None
        for i in range(left, right + 1):
            if val == inorder[i]:
                split = i
                break
        if split == None:
            return None
        
        node = TreeNode(val)
        self.preorder_pos += 1
        node.left = self.build_tree(preorder, inorder, left, split - 1)
        node.right = self.build_tree(preorder, inorder, split + 1, right)
        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_pos = 0
        return self.build_tree(preorder, inorder, 0, len(inorder) - 1)
