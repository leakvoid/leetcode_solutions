class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
            
        return (4294967296 % n == 0) and (2863311530 & n == 0)
