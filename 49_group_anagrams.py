from string import ascii_lowercase

class Solution:
    def hash_words(self, word):
        d_word = {}
        for c in ascii_lowercase:
            d_word[c] = 0
            
        for c in word:
            d_word[c] += 1
        
        res = ""
        for key in d_word:
            res += key * d_word[key]
        return res
    
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        d_words = {}
        for word in strs:
            key = self.hash_words(word)
            if key not in d_words:
                d_words[key] = []
            d_words[key].append(word)

        res = []
        for key in d_words:
            res.append(d_words[key])
        return res

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
