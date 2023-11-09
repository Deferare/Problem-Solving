class Solution {
    func numberOfWeakCharacters(_ properties: [[Int]]) -> Int {
        let sorted = properties.sorted {
            if $0[0] > $1[0] { return true }
            if $0[0] == $1[0] && $0[1] < $1[1] { return true }
            return false
        }
        
        var maxDefense = 0
        var weakCount = 0
        
        for num in sorted {
            if num[1] < maxDefense {
                weakCount += 1
            } else {
                maxDefense = num[1]
            }
        }
        
        return weakCount
    }
}
