class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += rem
            if digits[i] == 10:
                rem = 1
                digits[i] = 0
            else:
                rem = 0
                break
                
        if rem == 1:
            digits.insert(0, 1)
            
        return digits
