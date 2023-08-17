class Solution {
    func minDeletions(_ s: String) -> Int {
        var counter = Array(repeating: 0, count: 26)
        var answer = 0
        
        for c in s.unicodeScalars{
            let inx = Int(c.value) - 97
            counter[inx] += 1
        }
        
        counter.sort(by: >)
        
        for i in 1..<counter.count{
            if counter[i] >= counter[i-1]{
                answer += counter[i] - max(0, (counter[i-1] - 1))
                counter[i] = counter[i-1] - 1
            }else if counter[i] == 0 {break}
        }
        
        return answer
    }
}
