class Solution:
    def subsets_rec(self, nums, start, head, res):
        last_val = None
        for i in range(start, len(nums)):
            if nums[i] != last_val:
                last_val = nums[i]
                new_head = head.copy()
                new_head.append(nums[i])
                res.append(new_head)
                self.subsets_rec(nums, i + 1, new_head, res)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        self.subsets_rec(nums, 0, [], res)
        return res

