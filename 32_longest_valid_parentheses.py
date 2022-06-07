class Solution:
    def longestValidParentheses(self, s: str) -> int:
        beginning_idx = 0
        expected_closures = []
        
        max_length = 0
        cur_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                expected_closures.append(i)
            elif expected_closures and s[i] == ')':
                expected_closures.pop()          
            else:
                cur_length = i - beginning_idx
                    
                if cur_length > max_length:
                    max_length = cur_length
                
                expected_closures = []
                cur_length = 0
                beginning_idx = i + 1
                
        if expected_closures:
            prev = beginning_idx - 1
            expected_closures.append(len(s))
            for i in range(len(expected_closures)):
                cur_length = expected_closures[i] - prev - 1
                prev = expected_closures[i]
                if cur_length > max_length:
                    max_length = cur_length
        else:
            cur_length = len(s) - beginning_idx
        
        if cur_length > max_length:
            max_length = cur_length
            
        return max_length

s = Solution()
print(")))()()()(()()", s.longestValidParentheses(")))()()()(()()"))
print("(()", s.longestValidParentheses("(()"))
print(")()())", s.longestValidParentheses(")()())"))
print("()(()", s.longestValidParentheses("()(()"))
print("(()())", s.longestValidParentheses("(()())"))
print(")(((((()())()()))()(()))(((((((((", s.longestValidParentheses(")(((((()())()()))()(()))((((((((("))
print("(((((((()()()()()", s.longestValidParentheses("(((((((()()()()()"))
print("))(((((((()()()()()", s.longestValidParentheses("))(((((((()()()()()"))
print("()(()(((", s.longestValidParentheses("()(()((("))
print("((((()()(()(((", s.longestValidParentheses("((((()()(()((("))
print("((((()()((((()()()(((", s.longestValidParentheses("((((()()((((()()()((("))
