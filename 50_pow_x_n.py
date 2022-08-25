class Solution:
    def pow_rec(self, x, n):
        if n in self.memory:
            return self.memory[n]
        
        self.memory[n] = self.pow_rec(x, n // 2) * self.pow_rec(x, n // 2 + n % 2)
        return self.memory[n]
    
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            inverse_res = True
        else:
            inverse_res = False
        n = abs(n)
        
        if x < 0 and (n % 2) == 1:
            negative_res = True
        else:
            negative_res = False
        x = abs(x)
        
        self.memory = {}
        self.memory[1] = x
        
        res = self.pow_rec(x, n)
        
        if inverse_res:
            res = 1 / res
        if negative_res:
            res *= -1
        return res
