class Solution {
    func minNonZeroProduct(_ p: Int) -> Int {
        let mod = 1000000007
        let maxVal = (1 << p) - 1
        let secondMax = maxVal - 1
        let power = (1 << (p - 1)) - 1
        
        func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
            var result = 1
            var base = base % mod
            var exp = exp
            while exp > 0 {
                if exp % 2 == 1 {
                    result = (result * base) % mod
                }
                base = (base * base) % mod
                exp /= 2
            }
            return result
        }

        let productPart = modPow(secondMax, power, mod)
        let result = (productPart % mod) * (maxVal % mod) % mod
        
        return result
    }
}
