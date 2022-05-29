import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        s = str(x)
        l = len(s)
        if l < 2:
            return True
        
        if l % 2 == 0:
            low = int(l / 2 - 1)
            high = int(l / 2)
        else:
            low = int(math.floor(l / 2.0) - 1)
            high = int(math.ceil(l / 2.0))
            
        while low >= 0 and high < l:
            if s[low] != s[high]:
                return False
            low -= 1
            high += 1
            
        return True

s = Solution()
print("121:", "True" if s.isPalindrome(121) else "False")
print("31213:", "True" if s.isPalindrome(31213) else "False")
print("3321:", "True" if s.isPalindrome(3321) else "False")
print("197:", "True" if s.isPalindrome(197) else "False")
print("2020:", "True" if s.isPalindrome(2020) else "False")
print("2002:", "True" if s.isPalindrome(2002) else "False")
print("120029:", "True" if s.isPalindrome(120029) else "False")
