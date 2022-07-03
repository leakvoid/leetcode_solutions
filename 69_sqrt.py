class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        start = 0
        end = x
        mid = start + int((end - start) / 2)
        
        while (end - start) > 1:
            m = mid * mid
            if m == x:
                return mid
            elif m < x:
                start = mid
            else:
                end = mid
            mid = start + int((end - start) / 2)
        
        return mid

s = Solution()
print("4:", s.mySqrt(4))
print("8:", s.mySqrt(8))
print("81:", s.mySqrt(81))
