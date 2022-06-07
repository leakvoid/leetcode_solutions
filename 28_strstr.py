class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            flag = True
            for j in range(len(needle)):
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    flag = False
                    break
            if flag == True:
                return i
            
        return -1
