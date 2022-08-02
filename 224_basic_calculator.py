class Solution:
    char_to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
    def build_parantheses_map(self, s):
        self.p_map = {}
        p_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                p_stack.append(i)
            if s[i] == ')':
                self.p_map[p_stack.pop()] = i
    
    def parse(self, s, start, end):
        lval = 0
        sign = None
        i = start
        while i < end:
            match s[i]:
                case ' ':
                    i += 1
                    continue
                case '+':
                    i += 1
                    sign = '+'
                case '-':
                    i += 1
                    sign = '-'
                case '(':
                    if sign == '-':
                        lval -= self.parse(s, i+1, self.p_map[i])
                    else:
                        lval += self.parse(s, i+1, self.p_map[i])
                    i = self.p_map[i] + 1
                case ')':
                    i += 1
                    continue
                case _:
                    rval = self.char_to_digit[s[i]]
                    i += 1
                    
                    while i < len(s):
                        if s[i] in self.char_to_digit:
                            rval *= 10
                            rval += self.char_to_digit[s[i]]
                            i += 1
                        else:
                            break
                    
                    if sign == '-':
                        lval -= rval
                    else:
                        lval += rval
        return lval
    
    def calculate(self, s: str) -> int:
        self.build_parantheses_map(s)
        return self.parse(s, 0 , len(s))
