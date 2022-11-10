class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        note = dict()
        def recur(left, right):
            if left >= right: return 1
            if left > len(colors)//2: return 1
            if right < len(colors)//2: return 1
            key = left.__str__()+":"+right.__str__()
            if key in note:
                return 1
            note[key] = True
            leftColor = colors[left]
            rightColor = colors[right]
            if leftColor != rightColor: return abs(left-right)
            return max(recur(left+1, right), recur(left, right-1))
        return recur(0, len(colors)-1)
