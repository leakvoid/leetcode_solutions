import math

UPPER_BOUNDARY = 10000

class Solution:
    def squares_rec(self, n, rem_count):
        if rem_count == 0:
            return UPPER_BOUNDARY
        
        if n in self.memory:
            return self.memory[n]
        
        float_sqrt_n = math.sqrt(n)
        if float_sqrt_n.is_integer():
            self.memory[n] = 1
            return self.memory[n]
        
        rounded_sqrt_n = math.ceil(float_sqrt_n)
        min_count = UPPER_BOUNDARY
        for s in range(rounded_sqrt_n // 2, rounded_sqrt_n):
            new_n = n - pow(s, 2)
            cur_count = 1 + self.squares_rec(new_n, min_count - 1)
            if cur_count < min_count:
                min_count = cur_count
        
        self.memory[n] = min_count
        return self.memory[n]
    
    def numSquares(self, n: int) -> int:
        self.memory = {}
        return self.squares_rec(n, UPPER_BOUNDARY)
