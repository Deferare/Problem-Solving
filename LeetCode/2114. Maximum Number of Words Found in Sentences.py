class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for i in range(len(sentences)):
            num = len(list(sentences[i].split(" ")))
            if num > result: result = num
        return result
