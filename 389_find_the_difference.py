class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = {}
        for l in s:
            if l in s_counter:
                s_counter[l] += 1
            else:
                s_counter[l] = 1
        
        for l in t:
            if l not in s_counter:
                return l
            
            s_counter[l] -= 1
            if s_counter[l] < 0:
                return l
