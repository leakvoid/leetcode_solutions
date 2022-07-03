class Solution:
    def add(self, a, b):
        res = ""
        last_a = len(a) - 1
        last_b = len(b) - 1
        
        r = 0
        for i in range(len(a)):            
            a_val = 0 if a[last_a - i] == "0" else 1
            b_i = last_b - i
            b_val = 0 if b_i < 0 or b[b_i] == "0" else 1
        
            s_val = r + a_val + b_val
            if s_val == 0:
                res += "0"
                r = 0
            elif s_val == 1:
                res += "1"
                r = 0
            elif s_val == 2:
                res += "0"
                r = 1
            else:
                res += "1"
                r = 1
        
        if r == 1:
            res += "1"
                
        return res[::-1]
            
        
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            return self.add(a, b)
        else:
            return self.add(b, a)
