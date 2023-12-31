class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n > 1:
            if n % 2 == 1:
                total += (n - 1) / 2
                n = (n - 1) / 2 + 1
            else:
                total += n / 2
                n = n / 2
        
        return int(total)