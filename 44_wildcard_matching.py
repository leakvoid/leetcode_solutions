import re

class Solution:
    def memorize(self, s_i, p_i):
        if s_i in self.memory:
            self.memory[s_i].add(p_i)
        else:
            self.memory[s_i] = set()
            self.memory[s_i].add(p_i)
    
    def wildcard_match(self, s, p, s_i, p_i):
        if s_i in self.memory and p_i in self.memory[s_i]:
            return False
        
        if s_i >= len(s):
            self.memorize(s_i, p_i)
            return False
        
        pos = [m.start() for m in re.finditer('(?=' + p[p_i] + ')', s[s_i:])]
        
        for i in pos:
            if self.basic_match(s, p, s_i + len(p[p_i]) + i, p_i + 1):
                return True
        
        self.memorize(s_i, p_i)
        return False
    
    def basic_match(self, s, p, s_i, p_start):
        if s_i in self.memory and p_start in self.memory[s_i]:
            return False
        
        wildcard_flag = False
        for p_i in range(p_start, len(p)):
            if p[p_i] == '?':
                s_i += 1
            elif p[p_i] == '*':
                wildcard_flag = True
            elif wildcard_flag == False:
                p_len = len(p[p_i])
                if s_i + p_len > len(s):
                    self.memorize(s_i, p_i)
                    return False
                
                if s[s_i:s_i + p_len] == p[p_i]:
                    s_i += p_len
                else:
                    self.memorize(s_i, p_i)
                    return False
            else:
                return self.wildcard_match(s, p, s_i, p_i)
        
        if s_i > len(s):
            return False
        if wildcard_flag or s_i == len(s):
            return True
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        pp = []
        if p[0] == '*' or p[0] == '?':
            pp.append(p[0])
            ss = ""
        else:
            ss = p[0]

        for i in range(1, len(p)):
            if p[i] == '*' and  p[i-1] == '*':
                    continue
            
            if p[i] == '*' or p[i] == '?':
                if ss:
                    pp.append(ss)
                    ss = ""
                pp.append(p[i])
            else:
                ss += p[i]
        
        if ss:
            pp.append(ss)
        
        self.memory = {}
        return self.basic_match(s, pp, 0, 0)
    
'''
"aa"
"a"
"wfa"
"*?baa**t?lt*?*w**"
"aa"
"*"
"cb"
"?a"
"adfggtlalkt"
"?*gt*?kt*"
"asdf"
"?*d?"
"asdf"
"*?d?*"
"abcabczzzde"
"*abc???de*"
"aaaa"
"***a"
""
""
"a"
""
""
"*"
""
"?"
"abaab"
"*?a?"
"baaaa"
"*aaa"
'''
