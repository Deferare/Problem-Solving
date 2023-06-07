class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer, crnt, num_of_letters = [], [], 0
        for word in words:
            if num_of_letters + len(word) + len(crnt) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    crnt[i % (len(crnt) - 1 or 1)] += " "
                answer.append("".join(crnt))
                crnt, num_of_letters = [], 0
            crnt.append(word)
            num_of_letters += len(word)
        answer.append(" ".join(crnt).ljust(maxWidth))
        return answer
