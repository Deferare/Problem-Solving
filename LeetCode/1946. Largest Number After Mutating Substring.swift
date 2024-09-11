class Solution {
    func maximumNumber(_ num: String, _ change: [Int]) -> String {
        var result: [Character] = []
        var status: Int = 0
        
        for c in num {
            let d = Int(String(c))!
            
            if d >= change[d] || status == -1 {
                result.append(c)
                
                if status == 1 && d != change[d] {
                    status = -1
                }
            } else {
                result.append(Character(String(change[d])))
                status = 1
            }
        }
        
        return String(result)
    }
}
