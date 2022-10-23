class Solution:
    def process_word(self, lc_word, r, word, res):
        i = 1
        while i < len(lc_word):
            if lc_word[i] not in r:
                break
            i += 1
        if i == len(lc_word):
            res.append(word)

    def findWords(self, words: List[str]) -> List[str]:
        r1 = {'q','w','e','r','t','y','u','i','o','p'}
        r2 = {'a','s','d','f','g','h','j','k','l'}
        r3 = {'z','x','c','v','b','n','m'}

        res = []
        for word in words:
            lc_word = word.lower()
            if lc_word[0] in r1:
                self.process_word(lc_word, r1, word, res)
            elif lc_word[0] in r2:
                self.process_word(lc_word, r2, word, res)
            else:
                self.process_word(lc_word, r3, word, res)
        return res
