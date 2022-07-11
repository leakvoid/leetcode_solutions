# Definition for a binary tree node.
from copy import deepcopy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def to_str_rec(self, x):
        if x:
            s_l = self.to_str_rec(x.left)
            s_r = self.to_str_rec(x.right)
            if s_l == "None" and s_r == "None":
                return "TreeNode{val: " + str(x.val) + "}"
            else:
                return "TreeNode{val: " + str(x.val) + ", left:" + s_l + ", right:" + s_r + "}"

        else:
            return "None"
            
    def __str__(self):
        return self.to_str_rec(self.root)
    
    def __repr__(self):
        return self.to_str_rec(self.root)

    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right

        if y == None:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z

    def hash_key_rec(self, x):
        if x:
            s_l = self.hash_key_rec(x.left)
            s_r = self.hash_key_rec(x.right)
            if s_l == "n" and s_r == "n":
                return str(x.val)
            else:
                return str(x.val) + s_l + s_r
        else:
            return "n"
    
    def get_hash_key(self):
        return self.hash_key_rec(self.root)

class Solution:
    def generate_rec(self, nums, tree, res):
        key = tree.get_hash_key()
        if key in self.memory:
            return
        else:
            self.memory.add(key)

        if len(nums) == 0:
            res.append(tree)
            return
        
        for i in range(len(nums)):
            new_tree = deepcopy(tree)
            new_tree.insert( TreeNode(nums[i]) )
            self.generate_rec(nums[:i] + nums[i + 1:], new_tree, res)
    
    def generateTrees(self, n: int) -> [[TreeNode]]:
        nums = []
        for i in range(n):
            nums.append(i + 1)
        
        res = []
        self.memory = set()
        self.generate_rec(nums, Tree(), res)
        return res

s = Solution()
for n in range(8):
    res = s.generateTrees(n + 1)
    print(len(res))
#for r in res:
#    print(str(r))
