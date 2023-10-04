class Solution {
    func maxMatrixSum(_ matrix: [[Int]]) -> Int {
        var negCount = 0
        var minNum = Int.max
        var sumNum = 0
        
        for arr in matrix {
            for num in arr {
                if num < 0 { negCount+=1 }
                minNum = min(minNum, abs(num))
                sumNum += abs(num)
            }
        }

        if negCount%2 != 0 { sumNum -= (minNum+minNum) }
        
        return sumNum
    }
}
