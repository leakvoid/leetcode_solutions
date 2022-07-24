END_OF_WORD = '\n'

class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        node = self.head
        for l in word:
            if l not in node:
                node[l] = {}
            node = node[l]
        node[END_OF_WORD] = True

    def search(self, word: str) -> bool:
        node = self.head
        for l in word:
            if l not in node:
                return False
            node = node[l]
        return END_OF_WORD in node

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for l in prefix:
            if l not in node:
                return False
            node = node[l]
        return True
