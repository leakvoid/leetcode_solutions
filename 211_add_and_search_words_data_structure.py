END_OF_WORD = '\n'

class WordDictionary:

    def __init__(self):
        self.head = {}

    def addWord(self, word: str) -> None:
        node = self.head
        for l in word:
            if l not in node:
                node[l] = {}
            node = node[l]
        node[END_OF_WORD] = True

    def search(self, word: str, node = None) -> bool:
        if not node:
            node = self.head
        for i in range(len(word)):
            if word[i] == '.':
                for k in node:
                    if k == END_OF_WORD:
                        continue
                    if self.search(word[i + 1:], node[k]):
                        return True
                return False
            if word[i] not in node:
                return False
            node = node[word[i]]
        return END_OF_WORD in node


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
