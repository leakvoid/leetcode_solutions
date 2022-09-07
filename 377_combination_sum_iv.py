class Solution:
    def combination_rec(self, nums, target, tail):
        if target in self.memory:
            return self.memory[target]
        
        res = 0
        for n in nums:
            if (target - n) < 0:
                break
            
            tail.append(n)
            res += self.combination_rec(nums, target - n, tail)
            tail.pop()
        
        self.memory[target] = res
        return self.memory[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        self.memory = {}
        self.memory[0] = 1
        
        return self.combination_rec(nums, target, [])
