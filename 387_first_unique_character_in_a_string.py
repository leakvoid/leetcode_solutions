REPEATED_SYMBOL = 100001

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        
        for i in range(len(s)):
            l = s[i]
            if l in s_dict:
                s_dict[l] = REPEATED_SYMBOL
            else:
                s_dict[l] = i
        
        for key in s_dict:
            if s_dict[key] != REPEATED_SYMBOL:
                return s_dict[key]
        return -1
