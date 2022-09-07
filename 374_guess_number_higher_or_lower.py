# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guess_rec(self, start, end):
        mid = (start + end) // 2
        
        status = guess(mid)
        if status == 0:
            return mid
        elif status == -1:
            return self.guess_rec(start, mid - 1)
        return self.guess_rec(mid + 1, end)
    
    def guessNumber(self, n: int) -> int:
        return self.guess_rec(0, n)
