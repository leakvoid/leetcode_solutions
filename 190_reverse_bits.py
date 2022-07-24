class Solution:
    def reverseBits(self, n: int) -> int:
        s = '{:032b}'.format(n)
        return int(s[::-1], 2)
