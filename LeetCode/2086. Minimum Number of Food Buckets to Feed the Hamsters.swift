class Solution {
    func minimumBuckets(_ hamsters: String) -> Int {
        var hamsters = Array(hamsters)
        var answer = 0
        
        for i in 0..<hamsters.count {
            if hamsters[i] == "H" {
                if i > 0 && hamsters[i-1] == "F" { continue }
                if i < hamsters.count-1 && hamsters[i+1] == "." {
                    hamsters[i+1] = "F"
                    answer += 1
                } else if i > 0 && hamsters[i-1] == "." {
                    hamsters[i-1] = "F"
                    answer += 1
                } else { return -1 }
            }
        }
        
        return answer
    }
}
