class Solution {
    func minSwaps(_ s: String) -> Int {
        let chars = Array(s)
        var zeroNum = 0, oneNum = 0
        
        for c in s {
            if c == "0" { zeroNum += 1 }
            else { oneNum += 1 }
        }
        
        if abs(zeroNum - oneNum) >= 2 { return -1 }
        
        func countSwaps(startWith ch: Character) -> Int {
            var swaps = 0
            var current = ch
            for char in chars {
                if char != current {
                    swaps += 1
                }
                current = current == "0" ? "1" : "0"
            }
            return (swaps+1) / 2
        }
        
        if zeroNum == oneNum {
            return min(countSwaps(startWith: "0"), countSwaps(startWith: "1"))
        }

        return countSwaps(startWith: zeroNum > oneNum ? "0" : "1")
    }
}
