class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = x ^ y

        l = 0
        while r:
            if r % 2 == 1:
                l += 1
            r //= 2
        return l
