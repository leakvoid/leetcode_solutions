class Solution:
    char_to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
    def tokenize(self, s):
        tokens = []
        i = 0
        while i < len(s):
            match s[i]:
                case ' ':
                    i += 1
                    continue
                case '+' | '-' | '*' | '/':
                    tokens.append(s[i])
                    i += 1
                case _:
                    digit = self.char_to_digit[s[i]]
                    i += 1
                    while i < len(s):
                        if s[i] in self.char_to_digit:
                            digit *= 10
                            digit += self.char_to_digit[s[i]]
                            i += 1
                        else:
                            break
                    tokens.append(digit)
        if tokens[0] == '-':
            tokens.insert(0, 0)
        return tokens
                    
    def parse_first_priority_operators(self, tokens):
        res = []
        lval = tokens[0]
        for i in range(1, len(tokens) - 1, 2):
            if tokens[i] == '-' or tokens[i] == '+':
                res.append(lval)
                res.append(tokens[i])
                lval = tokens[i + 1]
            else:
                if tokens[i] == '*':
                    lval *= tokens[i + 1]
                elif tokens[i] == '/':
                    lval //= tokens[i + 1]
                else:
                    print("ERROR", tokens[i])
                    break
        res.append(lval)
        return res
    
    def parse_last_priority_operators(self, tokens):
        lval = tokens[0]
        for i in range(1, len(tokens) - 1, 2):
            if tokens[i] == '+':
                lval += tokens[i + 1]
            elif tokens[i] == '-':
                lval -= tokens[i + 1]
            else:
                print("ERROR", tokens[i])
                break
        return lval
    
    def calculate(self, s: str) -> int:
        return self.parse_last_priority_operators( self.parse_first_priority_operators( self.tokenize(s) ) )
