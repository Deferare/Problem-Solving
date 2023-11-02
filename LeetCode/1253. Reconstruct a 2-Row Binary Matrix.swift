class Solution {
    func reconstructMatrix(_ upper: Int, _ lower: Int, _ colsum: [Int]) -> [[Int]] {
        var upper = upper, lower = lower
        var answer: [[Int]] = [[], []]
        
        for sum in colsum {
            if sum == 2 {
                if upper == 0 || lower == 0 { return [] }
                answer[0].append(1)
                answer[1].append(1)
                upper -= 1
                lower -= 1
            } else if sum == 0 {
                answer[0].append(0)
                answer[1].append(0)
            } else if upper >= lower {
                if upper == 0 { return [] }
                answer[0].append(1)
                answer[1].append(0)
                upper -= 1
            } else if upper < lower {
                if lower == 0 { return [] }
                answer[0].append(0)
                answer[1].append(1)
                lower -= 1
            }
        }
        
        if upper != 0 || lower != 0 { return [] }
        
        return answer
    }
}
