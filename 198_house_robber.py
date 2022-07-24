class Solution:
    def robberies_remain(self, start, nums):
        if start >= len(nums):
            return 0
        
        if start in self.memory:
            return self.memory[start]
        
        self.memory[start] = nums[start] + max(self.robberies_remain(start + 2, nums), self.robberies_remain(start + 3, nums))
        return self.memory[start]
    
    def rob(self, nums: List[int]) -> int:
        self.memory = {}
        return max(self.robberies_remain(0, nums), self.robberies_remain(1, nums))
