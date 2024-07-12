class Solution {
    private func sumOfFirstK(_ k: Int) -> Int {
        return k * (k + 1) / 2
    }
    
    func minimumPossibleSum(_ n: Int, _ target: Int) -> Int {
        let mod = 1000000007
        
        if n < target / 2 {
            return sumOfFirstK(n) % mod
        }
        
        let remaining = n - target / 2
        let start = target - 1
        let end = start + remaining
        
        return (sumOfFirstK(target / 2) + sumOfFirstK(end) - sumOfFirstK(start)) % mod
    }
}
