class Solution {
    func longestSubsequence(_ s: String, _ k: Int) -> Int {
        let n = s.count
        let arr = Array(s)
        var dp = Array(repeating: 0, count: n+1)
        var ans = 0
        
        for i in 0..<n {
            let digit = Int(String(arr[i]))!
            if dp[ans] * 2 + digit <= k {
                let val = dp[ans] * 2 + digit
                ans += 1
                dp[ans] = val
            }
            
            for j in (1...ans).reversed() {
                dp[j] = min(dp[j], dp[j-1] * 2 + digit)
            }
        }
        return ans
    }
}
