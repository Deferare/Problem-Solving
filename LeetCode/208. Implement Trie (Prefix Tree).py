class Node:
    def __init__(self):
        self.d = dict()
        self.complet_check = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        crnt = self.root
        for i in range(len(word)):
            if word[i] not in crnt.d:
                crnt.d[word[i]] = Node()
            crnt = crnt.d[word[i]]
        crnt.complet_check = True

    def search(self, word: str) -> bool:
        crnt = self.root
        for i in range(len(word)):
            if word[i] not in crnt.d:
                return False
            crnt = crnt.d[word[i]]
        return crnt.complet_check

    def startsWith(self, prefix: str) -> bool:
        crnt = self.root
        for i in range(len(prefix)):
            if prefix[i] not in crnt.d:
                return False
            crnt = crnt.d[prefix[i]]
        return True
