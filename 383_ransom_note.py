import string

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l_counter = {}
        for l in string.ascii_lowercase:
            l_counter[l] = 0
        
        for l in magazine:
            l_counter[l] += 1
        
        for l in ransomNote:
            if l_counter[l] == 0:
                return False
            l_counter[l] -= 1
        
        return True
