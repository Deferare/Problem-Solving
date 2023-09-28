class Solution {
    func minOperations(_ n: Int) -> Int {
        var binary = String(n, radix: 2).map { return $0 }
        binary.reverse()
        binary.append("0")
        
        var result = 0
        var nest = 0
        var i = 0
        
        while i < binary.count {
            if binary[i] == "1" {
                nest += 1
                binary[i] = "0"
            } else {
                if nest > 1 {
                    binary[i] = "1"
                    i -= 1
                }
                result += min(nest, 1)
                nest = 0
            }
            i += 1
        }
        
        result += min(nest, 1)
        
        return result
    }
}
