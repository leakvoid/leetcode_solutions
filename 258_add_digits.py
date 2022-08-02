class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            n_num = 0
            while num > 0:
                n_num += num % 10
                num //= 10
            num = n_num
        return num
