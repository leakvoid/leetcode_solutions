class Solution:
    def rob_house(self, nums, start, end):
        if start > end:
            return 0
        
        if start in self.memory[end]:
            return self.memory[end][start]
        
        self.memory[end][start] = nums[start] + max(self.rob_house(nums, start + 2, end),
                                                    self.rob_house(nums, start + 3, end))
        return self.memory[end][start]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        self.memory = {}
        self.memory[len(nums) - 1] = {}
        self.memory[len(nums) - 2] = {}
        
        return max(self.rob_house(nums, 0, len(nums) - 2),
                   self.rob_house(nums, 1, len(nums) - 1),
                   self.rob_house(nums, 2, len(nums) - 1))
