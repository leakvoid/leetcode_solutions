class Solution:
    char_to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
    def tokenize(self, expression):
        res = []
        i = 0
        while i < len(expression):
            match expression[i]:
                case '+' | '-' | '*':
                    res.append(expression[i])
                    i += 1
                case _:
                    d = self.char_to_digit[expression[i]]
                    i += 1
                    while i < len(expression):
                        if expression[i] not in self.char_to_digit:
                            break
                        d *= 10
                        d += self.char_to_digit[expression[i]]
                        i += 1
                    res.append(d)
        return res
    
    def parse_rec(self, tokens, start, end):
        if start == end:
            return [tokens[start]]
        
        if end in self.memory[start]:
            return self.memory[start][end]
        
        res = []
        for mid in range(start + 1, end, 2):
            r1 = self.parse_rec(tokens, start, mid - 1) 
            r2 = self.parse_rec(tokens, mid + 1, end)
            for i in range(len(r1)):
                for j in range(len(r2)):
                    match tokens[mid]:
                        case '+':
                            r = r1[i] + r2[j]
                        case '-':
                            r = r1[i] - r2[j]
                        case '*':
                            r = r1[i] * r2[j]
                    res.append(r)
        
        self.memory[start][end] = res
        return res
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens = self.tokenize(expression)
        
        self.memory = {}
        for i in range(len(tokens)):
            self.memory[i] = {}
        
        return self.parse_rec(tokens, 0, len(tokens) - 1)
