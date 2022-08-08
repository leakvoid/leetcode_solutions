# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def bin_search(self, start, end):
        mid = (start + end) // 2
        
        if isBadVersion(mid):
            if mid == 1:
                return 1
            if not isBadVersion(mid - 1):
                return mid
            
            return self.bin_search(start, mid - 1)
        return self.bin_search(mid + 1, end)
    
    def firstBadVersion(self, n: int) -> int:
        return self.bin_search(1, n)
