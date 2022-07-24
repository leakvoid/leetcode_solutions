class Solution:
    def is_palindrome(self, s, start, end):
        left = start
        right = end
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def fragment(self, s, start, end):
        if end in self.memory[start]:
            return (self.memory[start][end], True)

        if start == end:
            self.memory[start][end] = [[s[start]]]
            return (self.memory[start][end], False)

        res = []
        if self.is_palindrome(s, start, end):
            res.append( [s[start:end + 1]] )
        
        for split in range(start, end):
            (l_res, l_from_memory) = self.fragment(s, start, split)
            (r_res, r_from_memory) = self.fragment(s, split + 1, end)
            for l in l_res:
                for r in r_res:
                    if not l_from_memory or not r_from_memory:
                        res.append(l + r)
        
        self.memory[start][end] = res
        return (self.memory[start][end], False)
            
    
    def partition(self, s: str) -> List[List[str]]:
        self.memory = {}
        for i in range(len(s)):
            self.memory[i] = {}
        
        (res, from_memory) = self.fragment(s, 0, len(s) - 1)
        return res
