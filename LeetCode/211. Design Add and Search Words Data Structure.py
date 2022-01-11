class TrieNode():
    def __init__(self):
        self.d = dict()
        self.check = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        crnt = self.root
        for i in range(len(word)):
            if word[i] not in crnt.d:
                crnt.d[word[i]] = TrieNode()
            if i == len(word) - 1: crnt.check = True
            crnt = crnt.d[word[i]]

    def search(self, word: str) -> bool:
        tries = [self.root]
        index = 0
        while index < len(word) - 1:
            tries_next = []
            while len(tries) > 0:
                trie = tries.pop()
                if word[index] == ".":
                    for val in trie.d.values():
                        tries_next.append(val)
                elif word[index] in trie.d:
                    tries_next.append(trie.d[word[index]])
                else: continue
            if len(tries_next) > 0:
                tries = tries_next.copy()
                index += 1
            else: break
        while len(tries) > 0:
            pop = tries.pop()
            if (word[index] == "." or word[index] in pop.d) and pop.check:
                return True
        return False
