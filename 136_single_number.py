class Solution:
    def singleNumber(self, nums: [int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor

s = Solution()
print([1,2,3,4,2,3,1], s.singleNumber([1,2,3,4,2,3,1]))
