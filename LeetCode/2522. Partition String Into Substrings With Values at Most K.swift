class Solution {
    func minimumPartition(_ s: String, _ k: Int) -> Int {
        var answer = 0
        var crnt = 0
        
        for char in s {
            crnt = crnt * 10 + Int(String(char))!
            if crnt > k {
                answer += 1
                crnt = Int(String(char))!
            }
            if crnt > k {
                return -1
            }
        }
        
        return answer + 1
    }
}
