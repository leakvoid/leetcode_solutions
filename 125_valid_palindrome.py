import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #digits = set(map(lambda n : str(n), range(10)))
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        s = s.lower()
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in string.ascii_lowercase and s[left] not in digits:
                left += 1
                continue
            if s[right] not in string.ascii_lowercase and s[right] not in digits:
                right -= 1
                continue
                
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

s = Solution()
print("A man, a plan, a canal: Panama", s.isPalindrome("A man, a plan, a canal: Panama"))
print("race a car", s.isPalindrome("race a car"))
