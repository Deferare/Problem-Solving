class Solution {
    func mergeTriplets(_ triplets: [[Int]], _ target: [Int]) -> Bool {
        var isPossible = [false, false, false]
        
        for triplet in triplets {
            if (triplet[0] > target[0]) || (triplet[1] > target[1]) || (triplet[2] > target[2]) {
                continue
            }
            
            for i in 0..<3 {
                if triplet[i] == target[i] {
                    isPossible[i] = true
                }
            }
            
            if isPossible[0] && isPossible[1] && isPossible[2] {
                return true
            }
        }
        
        return false
    }
}
