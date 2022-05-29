class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        h = set()
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] in h:
                h.remove(s[i])
                i += 1
            else:
                h.add(s[j])
                j += 1
                max_length = max(max_length, j - i)        
        return max_length

s = Solution()
str = "abcabcbb"
print("input:", str)
print("result:", s.lengthOfLongestSubstring(str))
