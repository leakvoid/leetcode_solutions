class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match = {}
        used_symbols = set()
        for i in range(len(s)):
            if s[i] not in match:
                if t[i] in used_symbols:
                    return False
                match[s[i]] = t[i]
                used_symbols.add(t[i])
            elif t[i] != match[s[i]]:
                return False
        
        return True
