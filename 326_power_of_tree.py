class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # without loop pow(3, 21) > pow(2, 31)
        return (10460353203 % n == 0)
        
    def with_loop(self, n):
        if n <= 0:
            return False
        
        while n > 1:
            if n % 3:
                return False
            n //= 3
        
        return True
