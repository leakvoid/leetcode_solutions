
WORD_END = '\n'
IN_DICT = 1
NOT_A_WORD = 2
BOTTOM_REACHED = 3

class Solution:
    def check_dict(self, s, start, end):
        node = self.prefix_tree
        for i in range(start, end + 1):
            if s[i] not in node:
                return BOTTOM_REACHED
            node = node[s[i]]
        if WORD_END in node:
            return IN_DICT
        else:
            return NOT_A_WORD
        
    def match_to_dict(self, s, start):
        if start in self.memory:
            return False
        
        if start == len(s):
            return True
        
        end = start
        while end < len(s):
            status = self.check_dict(s, start, end)
            if status == BOTTOM_REACHED:
                self.memory.add(start)
                return False
            elif status == IN_DICT:
                if self.match_to_dict(s, end + 1):
                    return True
            end += 1

        self.memory.add(start)
        return False
    
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        self.memory = set()
        
        self.prefix_tree = {}
        for word in wordDict:
            node = self.prefix_tree
            for l in word:
                if l not in node:
                    node[l] = {}
                node = node[l]
            node[WORD_END] = None
        
        return self.match_to_dict(s, 0)

s = Solution()
print('s = "leetcode", wordDict = ["leet","code"]:', s.wordBreak("leetcode", ["leet","code"]))
print('s = "applepenapple", wordDict = ["apple","pen"]', s.wordBreak("applepenapple", ["apple","pen"]))
print('s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]', s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print('"a", ["a"]', s.wordBreak("a", ["a"]))
print('"a", ["b"]', s.wordBreak("a", ["b"]))
print('"fooleo", ["fool", "foo", "leod"]', s.wordBreak("fooleo", ["fool", "foo", "leod"]))
print('"fooleodd", ["fool", "foo", "leod"]', s.wordBreak("fooleo", ["fool", "foo", "leod"]))
