import math

class Solution:
    def findComplement(self, num: int) -> int:
        base = math.floor(math.log2(num))
        ones = pow(2, base + 1) - 1

        return num ^ ones
