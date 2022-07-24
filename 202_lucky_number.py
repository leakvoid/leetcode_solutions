class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        found.add(n)

        while True:
            s = str(n)
            n = 0
            for l in s:
                d = int(l)
                n += d ** 2
            if n == 1:
                return True
            if n in found:
                return False
            found.add(n)

class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        found.add(n)
        
        while True:
            new_n = 0
            while n:
                d = n % 10
                new_n += d ** 2
                n //= 10
            if new_n == 1:
                return True
            if new_n in found:
                return False
            found.add(new_n)
            n = new_n


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
print(s.isHappy(1234643))
print(s.isHappy(124543))
print(s.isHappy(2343))
print(s.isHappy(12436))
print(s.isHappy(32147))
print(s.isHappy(4668))
print(s.isHappy(4668))
print(s.isHappy(12))
print(s.isHappy(65))
