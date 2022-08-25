
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BST_insert(self, node, val):
        if val <= node.val:
            if node.left:
                self.BST_insert(node.left, val)
            else:
                node.left = TreeNode(val)
                return node.left
        else:
            if node.right:
                self.BST_insert(node.right, val)
            else:
                node.right = TreeNode(val)
                return node.right
                
    def dac_insert(self, nums, node, start, end):
        if start > end:
            return
        
        mid = (end + start) // 2
        node = self.BST_insert(node, nums[mid])
        
        self.dac_insert(nums, node, start, mid - 1)
        self.dac_insert(nums, node, mid + 1, end)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        self.dac_insert(nums, root, 0, mid - 1)
        self.dac_insert(nums, root, mid + 1, len(nums) - 1)
        
        return root
