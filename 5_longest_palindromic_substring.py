class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2:
            return s
        
        max_palindrom_len = 0
        max_palindrom_start = 0
        for i in range(len(s)):
            low = i - 1
            high = i + 1
            while high < len(s) and s[i] == s[high]:
                high += 1

            while low >= 0 and s[i] == s[low]:
                low -= 1

            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1

            palindrom_len = high - low - 1
            if palindrom_len > max_palindrom_len:
                max_palindrom_len = palindrom_len
                max_palindrom_start = low + 1

        return s[max_palindrom_start:(max_palindrom_start + max_palindrom_len)]
            
            # j = 0
            # while (i - j) >= 0 and (i + j) < len(s):
            #     if s[i - j] == s[i + j]:
            #         palindrom_len = 1 + 2 * j
            #         j += 1
            #     else:
            #         break
            # if palindrom_len > max_palindrom_len:
            #     max_palindrom_len = palindrom_len
            #     max_palindrom_start = i - j + 1

            # j = 0
            # while (i - j) >= 0 and (i + j + 1) < len(s):
            #     if s[i - j] == s[i + j + 1]:
            #         palindrom_len = 2 + 2 * j
            #         j += 1
            #     else:
            #         break
            # if palindrom_len > max_palindrom_len:
            #     max_palindrom_len = palindrom_len
            #     max_palindrom_start = i - j + 1

e = Solution()
print('"babad":', e.longestPalindrome("babad"))
print('"qcddcr":', e.longestPalindrome("qcddcr"))
print('"cbbd":', e.longestPalindrome("cbbd"))
print('"a":', e.longestPalindrome("a"))
print('"ccc":', e.longestPalindrome("ccc"))
