class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        
        res = 0
        for b in s:
            if b == '1':
                res += 1
        return res
