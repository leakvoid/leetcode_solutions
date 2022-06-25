class PermutationTree:
    def __init__(self, d):
        self.root = {}
        self.depth = d
    
    def add_unique(self, a):
        node = self.root
        last_idx = len(a) - 1
        for i in range(last_idx):
            val = a[i]
            if val not in node:
                if i == last_idx - 1:
                    node[val] = a[last_idx]
                else:
                    node[val] = {}
            node = node[val]
    
    def to_array_rec(self, res, node, stack):
        if len(stack) == self.depth - 1:
            stack.append(node)
            res.append(stack)
            return
        
        for key in node:
            new_stack = stack.copy()
            new_stack.append(key)
            self.to_array_rec(res, node[key], new_stack)
        
    def to_array(self):
        res = []
        self.to_array_rec(res, self.root, [])
        return res

class Solution:
    def rec_permute(self, res, tail, head):
        if len(head) == 1:
            tail.append(head[0])
            res.add_unique(tail)
            return
        
        for i in range(len(head)):
            new_tail = tail.copy()
            new_tail.append(head[i])
            
            self.rec_permute(res, new_tail, head[:i] + head[i+1:])
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            res = []
            res.append(nums)
            return res
        
        res = PermutationTree(len(nums))
        self.rec_permute(res, [], nums)
        return res.to_array()
