MIN_INT = -1 * pow(2, 31)
MAX_INT = pow(2, 31) - 1

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        res = 0
        for bit in range(32):
            s = 0
            for i in range(len(nums)):
                s += nums[i] & (1 << bit)
            if s % 3 != 0:
                res |= (1 << bit)
                
        if res > MAX_INT:
            res = res + MIN_INT - MAX_INT - 1
        return res

s = Solution()
print([2,2,3,2], s.singleNumber([2,2,3,2]))
print([0,1,0,1,0,1,99], s.singleNumber([0,1,0,1,0,1,99]))
