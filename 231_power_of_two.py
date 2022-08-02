import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 > 0:
                return False
            n /= 2
        return True
    
    def isPowerOfTwo_noloop(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return (math.log2(n)).is_integer()
