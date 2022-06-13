class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -100000
        c_sum = 0
        for n in nums:
            c_sum += n
            if c_sum > max_sum:
                max_sum = c_sum
            if c_sum < 0:
                c_sum = 0
                
        return max_sum
