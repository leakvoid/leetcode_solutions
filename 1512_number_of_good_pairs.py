class Solution:
    def numIdenticalPairs(self, nums) -> int:
        num_hash = {}
        res = 0
        for n in nums:
            if n not in num_hash:
                num_hash[n] = 1
            else:
                res += num_hash[n]
                num_hash[n] += 1
        
        return res