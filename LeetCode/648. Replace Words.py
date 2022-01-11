class TrieNode:
    def __init__(self):
        self.d = dict()
        self.wCheck = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        crnt = self.root
        for i in range(len(word)):
            if word[i] not in crnt.d:
                crnt.d[word[i]] = TrieNode()
            crnt = crnt.d[word[i]]
            if i == len(word) - 1: crnt.wCheck = True

    def wordGet(self, word):
        crnt = self.root
        for i in range(len(word)):
            if word[i] not in crnt.d:
                return word
            if crnt.d[word[i]].wCheck:
                return word[:i + 1]
            crnt = crnt.d[word[i]]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for i in range(len(dictionary)):
            trie.insert(dictionary[i])
        sentences = list(map(str, sentence.split(" ")))
        for i in range(len(sentences)):
            sentences[i] = trie.wordGet(sentences[i])
        result = ""
        for i in range(len(sentences)):
            result += sentences[i]
            if i != len(sentences) - 1:
                result += " "
        return result
