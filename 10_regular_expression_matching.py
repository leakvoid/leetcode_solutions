class Solution:
    def parse_pattern(self, p):
        res = []
        
        i = len(p) - 1
        while i >= 0:
            if p[i] == '*' and (i - 1) >= 0:
                if len(res) < 1 or res[-1]['val'] != p[i - 1] or res[-1]['rep'] !=  p[i]:
                    res.append({'val': p[i - 1], 'rep': p[i]})
                i -= 2
            else:
                res.append({'val': p[i], 'rep': 1})
                i -= 1
        res.reverse()
        return res

    def star_match(self, p, s, i, j):
        results = []
        results.append( self.match_pattern(p, s, i + 1, j) )# 0 repetition case
        
        while j < len(s) and (p[i]['val'] == '.' or p[i]['val'] == s[j]):# inefficient
            res = self.match_pattern(p, s, i + 1, j + 1)
            results.append(res)
            j += 1
            
        for r in results:
            if r:
                return True
        return False
    
    def match_pattern(self, p, s, i = 0, j = 0):
        while i < len(p):
            if p[i]['rep'] == '*':
                return self.star_match(p, s, i, j)
            elif j < len(s) and (p[i]['val'] == '.' or p[i]['val'] == s[j]):
                i += 1
                j += 1
            else:
                return False
            
        if i == len(p) and j == len(s):
            return True
        else:
            return False
        
    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.parse_pattern(p)
        return self.match_pattern(pattern, s)
