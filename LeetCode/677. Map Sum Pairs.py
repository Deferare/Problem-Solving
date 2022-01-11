from collections import deque

class TrieNode:
    def __init__(self):
        self.word_check = False
        self.value = 0
        self.d = dict()

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        crnt = self.root
        for i in range(len(key)):
            if key[i] not in crnt.d:
                crnt.d[key[i]] = TrieNode()
            crnt = crnt.d[key[i]]
            if i == len(key) - 1:
                crnt.word_check = True
                crnt.value = val

    def sum(self, prefix: str) -> int:
        crnt = self.root
        for i in range(len(prefix)):
            if prefix[i] not in crnt.d: return 0
            else: crnt = crnt.d[prefix[i]]
        result = 0
        q = deque([crnt])
        while len(q) > 0:
            q_next = deque()
            while len(q) > 0:
                pop = q.popleft()
                if pop.word_check:
                    result += pop.value
                for item in pop.d.values():
                    q_next.append(item)
            q = q_next
        return result
