class Solution:
    digit_to_letters = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h', 'i'],
        '5': ['j','k','l'],
        '6': ['m', 'n', 'o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }
    
    def digits_to_combinations(self, res, digits, prev_seq = ''):        
        if len(digits) < 1:
            res.append( prev_seq )
        else:
            for l in self.digit_to_letters[digits[0]]:
                self.digits_to_combinations(res, digits[1:], prev_seq + str(l))
    
    def letterCombinations(self, digits: str):
        res = []
        self.digits_to_combinations(res, digits)
        return res

s = Solution()
print('"23":', s.letterCombinations("23"))
print('"257":', s.letterCombinations("257"))
