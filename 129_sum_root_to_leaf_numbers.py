# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse_rec(self, x, nums):
        if x:
            if not x.left and not x.right:
                res = x.val
                p = 1
                for n in range(len(nums) - 1, -1, -1):
                    res += pow(10, p) * nums[n]
                    p += 1
                return res
            
            nums.append(x.val)
            l_sum = self.traverse_rec(x.left, nums)
            r_sum = self.traverse_rec(x.right, nums)
            nums.pop()
            
            return l_sum + r_sum
        else:
            return 0
    
    def sumNumbers(self, root: [TreeNode]) -> int:
        nums = []
        return self.traverse_rec(root, nums)

s = Solution()
print("[1,2,3]", s.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
