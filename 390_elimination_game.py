class Solution:
    def half_rec(self, n, ltr_flag):
        if n == 1:
            return 0
        
        if n % 2 or ltr_flag:
            return 2 * self.half_rec(n // 2, not ltr_flag) + 1
        return 2 * self.half_rec(n // 2, True)
    
    def lastRemaining(self, n: int) -> int:
        return self.half_rec(n, True) + 1
