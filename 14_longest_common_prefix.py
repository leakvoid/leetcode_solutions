class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        res = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return res
            res += strs[0][i]
            
        return res

s = Solution()
print('["flower","flow","flight"]:', s.longestCommonPrefix(["flower","flow","flight"]))
