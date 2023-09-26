class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        var dp = [0,Int.min,Int.min]
        
        for num in nums {
            var temp = dp
            for i in 0..<3 {
                temp[(i+num)%3] = max(dp[(i+num)%3], dp[i]+num)
            }
            dp = temp
        }
        
        return dp[0]
    }
}
