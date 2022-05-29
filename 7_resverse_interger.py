
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        s = str(x)
        res = []
        
        if s[0] == '-':
            res.append('-')
            bound = 1
        else:
            bound = 0
        
        i = len(s) - 1
        while i >= bound:
            res.append(s[i])
            i -= 1
        
        int_res = int(''.join(res))
        if int_res > (pow(2, 31) - 1) or int_res < -pow(2, 31):
            return 0
        else:
            return int_res

s = Solution()
print("123", s.reverse(123))
print("-123", s.reverse(-123))
print("120", s.reverse(120))
print("11987654321", s.reverse(11987654321))
