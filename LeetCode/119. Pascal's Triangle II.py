class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        crnt = []
        for i in range(1, rowIndex+1):
            crnt.append(1)
            for j in range(1, i):
                crnt.append(pre[j-1]+pre[j])
            crnt.append(1)
            pre = crnt.copy()
            crnt.clear()
        return pre
