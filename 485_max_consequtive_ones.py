class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons_ones = 0
        cons_ones = 0
        for n in nums:
            if n == 1:
                cons_ones += 1
            else:
                if cons_ones > max_cons_ones:
                    max_cons_ones = cons_ones
                cons_ones = 0
        return max(max_cons_ones, cons_ones)
