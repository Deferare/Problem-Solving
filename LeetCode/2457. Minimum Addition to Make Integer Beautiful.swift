class Solution {
    func makeIntegerBeautiful(_ n: Int, _ target: Int) -> Int {
        var crntN = n
        var added = 0
        var multiplier = 1
        
        func digitSum(_ num: Int) -> Int {
            return String(num).reduce(0) {
                $0 + Int(String($1))!
            }
        }
        
        while digitSum(crntN) > target {
            let reminder = crntN % 10
            let toAdd = 10 - reminder
            
            added += toAdd * multiplier
            crntN = (crntN + toAdd) / 10
            multiplier *= 10
        }
        
        return added
    }
}
