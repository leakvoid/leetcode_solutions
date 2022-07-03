class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        f1 = 1
        f2 = 2
        k = 2
        while k < n:
            f1, f2 = f2, f1 + f2
            k +=1
            
        return f2
