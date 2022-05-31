class Solution:
    opening_symbols = {'(', '{', '['}
    opening_to_closing = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    def isValid(self, s: str) -> bool:
        expected_stack = []
        for cs in s:
            if cs in self.opening_symbols:
                expected_stack.append(self.opening_to_closing[cs])
            elif expected_stack and cs == expected_stack[-1]:
                expected_stack.pop()
            else:
                return False
            
        if not expected_stack:
            return True
        return False

s = Solution()
print("{{}[][[[]]]}:", s.isValid("{{}[][[[]]]}"))
print("}:", s.isValid("}"))
