class Solution:
    def subsets_rec(self, nums, start, head, res):
        for i in range(start, len(nums)):
            new_head = head.copy()
            new_head.append(nums[i])
            res.append(new_head)
            self.subsets_rec(nums, i + 1, new_head, res)
            
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.subsets_rec(nums, 0, [], res)
        return res
