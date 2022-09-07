class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        mid = len(s) // 2
        
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vovels:
                while j > i:
                    if s[j] in vovels:
                        s[i], s[j] = s[j], s[i]
                        j -= 1
                        break
                    j -= 1
            i += 1
        
        return "".join(s)
