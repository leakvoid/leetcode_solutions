
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        res = 0;
        for i in range(len(s) - 1):
            l_c = roman_dict[s[i]]
            l_n = roman_dict[s[i + 1]]
            if l_c < l_n:
                res -= l_c
            else:
                res += l_c
        res += roman_dict[s[-1]]
        
        return res

s = Solution()
i = "MCMXCIV"
print("input:", i)
print("output:", s.romanToInt(i))
