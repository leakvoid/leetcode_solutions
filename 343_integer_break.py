class Solution:
    def integer_break_rec(self, n):
        if n in self.memory:
            return self.memory[n]
        
        max_m = 1
        for i in range(1, n + 1):
            m = i * self.integer_break_rec(n - i)
            if m > max_m:
                max_m = m
        
        self.memory[n] = max_m
        return self.memory[n]
    
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3: 
            return 2
        
        self.memory = {}
        
        return self.integer_break_rec(n)
