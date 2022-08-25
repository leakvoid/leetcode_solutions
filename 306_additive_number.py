class Solution:
    def check_sequence(self, first_n, second_n, num):
        if len(first_n) > 1 and first_n[0] == '0':
            return False
        if len(second_n) > 1 and second_n[0] == '0':
            return False
        
        if len(num) == 0:
            return True
        
        bound = max(len(first_n), len(second_n))
        sum_n = int(first_n) + int(second_n)
        if sum_n == int(num[:bound]):
            return self.check_sequence(second_n, num[:bound], num[bound:])
        elif sum_n == int(num[:bound+1]):
            return self.check_sequence(second_n, num[:bound+1], num[bound+1:])
        return False
    
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        l = len(num) * 2 // 3
        
        for i in range(1, l):
            first_n = num[:i]
            for j in range(1, l - i + 1):
                second_n = num[i:i+j]
                if self.check_sequence(first_n, second_n, num[i+j:]):
                    return True
        
        return False
