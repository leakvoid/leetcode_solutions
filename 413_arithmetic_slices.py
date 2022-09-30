class Solution:
    def count_sequences(self, l):
        s = len(self.dp)
        if l < s:
            return self.dp[l]
        
        for i in range(s, l + 1):
            self.dp.append(self.dp[-1] + i - 2)
        
        return self.dp[-1]
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        
        if len(nums) == 1:
            return res
        
        self.dp = [0,0]
        
        start = 0
        step = nums[1] - nums[0]
        for i in range(2, len(nums)):
            new_step = nums[i] - nums[i - 1]
            if new_step != step:
                res += self.count_sequences(i - start)
                step = new_step
                start = i - 1
        
        res += self.count_sequences(len(nums) - start)
        return res
