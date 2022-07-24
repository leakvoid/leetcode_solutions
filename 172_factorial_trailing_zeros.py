class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        
        p = 5
        while True:
            d = n // p
            if d == 0:
                return res
            res += d
            p *= 5
