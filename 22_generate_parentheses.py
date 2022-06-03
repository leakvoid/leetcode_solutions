class Solution:
    def gen_parentheses_seq(self, cur, opening, closing):
        if opening == 0 and closing == 0:
            return [cur]
        
        res = []
        if opening > 0:
            res += self.gen_parentheses_seq(cur + '(', opening - 1, closing)
        if closing > 0 and (closing - 1) >= opening:
            res += self.gen_parentheses_seq(cur + ')', opening, closing - 1)
        return res
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.gen_parentheses_seq('(', n - 1, n)

s = Solution()
print(s.generateParenthesis(4))
