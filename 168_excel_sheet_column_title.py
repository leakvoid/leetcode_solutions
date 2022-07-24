import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_to_letter = {}
        num_to_letter[0] = 'Z'
        for i in range(26):
            num_to_letter[i + 1] = string.ascii_uppercase[i]
        
        res = ""
        while columnNumber > 0:
            rem = columnNumber % 26
            res = num_to_letter[rem] + res
            if rem == 0:
                columnNumber -= 26
            columnNumber = columnNumber // 26
            
        return res
