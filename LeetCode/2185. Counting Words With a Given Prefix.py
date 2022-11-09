class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if len(word) < len(pref): continue
            pref_word = ""
            for i in range(0, len(pref)):
                pref_word += word[i]
            if pref_word == pref: count+= 1
        return count
