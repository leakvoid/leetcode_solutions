class Solution:
    def bin_search(self, start, end, target):
        if start > end:
            return False
        
        mid = (start + end) // 2
        
        squared = mid * mid
        if squared == target:
            return True
        elif squared > target:
            return self.bin_search(start, mid - 1, target)
        return self.bin_search(mid + 1, end, target)
    
    def isPerfectSquare(self, num: int) -> bool:
        return self.bin_search(0, num, num)
