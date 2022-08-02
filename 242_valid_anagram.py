class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram_hashmap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_ctr = {}
        for l in s:
            if l in char_ctr:
                char_ctr[l] += 1
            else:
                char_ctr[l] = 1
                
        for l in t:
            if l in char_ctr and char_ctr[l] > 0:
                char_ctr[l] -= 1
            else:
                return False
        return True
