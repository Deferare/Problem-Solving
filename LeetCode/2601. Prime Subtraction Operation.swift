class Solution {
    private func isPrime(_ n: Int) -> Bool {
        if n <= 1 { return false }
        if n <= 3 { return true }
        if n % 2 == 0 || n % 3 == 0 { return false }
        
        var i = 5
        
        while i * i <= n {
            if n % i == 0 || n % (i + 2) == 0 { return false }
            i += 6
        }
        
        return true
    }
    
    private func getNextPrime(_ crnt: Int,_ preMax: Int) -> Int? {
        if crnt <= 2 { return nil }
        
        var minPrime: Int? = nil
        
        for num in stride(from: crnt, to: 1, by: -1) {
            if isPrime(num) && crnt - num > preMax {
                minPrime = crnt - num
                
                break
            }
        }
        
        return minPrime
    }
    
    func primeSubOperation(_ nums: [Int]) -> Bool {
        var preMax = nums[0]
        
        if let prime = getNextPrime(nums[0], 0) {
            preMax = prime
        }
        
        for i in 1..<nums.count {
            var next = nums[i]
            
            if let prime = getNextPrime(next, preMax) {
                next = prime
            }
            
            if next <= preMax {
                return false
            }
            
            preMax = next
        }
        
        return true
    }
}
