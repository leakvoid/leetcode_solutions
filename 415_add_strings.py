class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s_to_d = {}
        d_to_s = []
        for i in range(10):
            s_to_d[str(i)] = i
            d_to_s.append( str(i) )
        
        res = ""
        i = 0
        rem = 0
        while i < len(num1) and i < len(num2):
            n1 = s_to_d[ num1[-1 - i] ]
            n2 = s_to_d[ num2[-1 - i] ]
            r = rem + n1 + n2
            rem = 1 if r > 9 else 0
            res += d_to_s[ r % 10 ]
            i += 1
        
        while i < len(num1):
            n1 = s_to_d[ num1[-1 - i] ]
            r = rem + n1
            rem = 1 if r > 9 else 0
            res += d_to_s[ r % 10 ]
            i += 1

        while i < len(num2):
            n2 = s_to_d[ num2[-1 - i] ]
            r = rem + n2
            rem = 1 if r > 9 else 0
            res += d_to_s[ r % 10 ]
            i += 1
        
        if rem:
            res += "1"
        
        return res[::-1]
