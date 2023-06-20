class Solution {
    func minWindow(_ s: String, _ t: String) -> String {
        let sArray = Array(s)
        var minLen = Int.max
        var tCounter = Dictionary<Character, Int>()
        
        for c in t{
            tCounter[c, default: 0] += 1
        }
        
        var tcount = tCounter.count
        var left = 0
        var minLeft = 0
        var right = 0
        
        while right < sArray.count{
            let c = sArray[right]
            if let count = tCounter[c]{
                tCounter[c] = count - 1
                if tCounter[c]! == 0{
                    tcount -= 1
                }
            }
            
            right += 1
            
            while tcount == 0{
                if right - left < minLen{
                    minLen = right - left
                    minLeft = left
                }
                let c2 = sArray[left]
                if let count = tCounter[c2]{
                    tCounter[c2] = count + 1
                    if tCounter[c2]! == 1{
                        tcount += 1
                    }
                }
                left += 1
            }
        }
        
        if minLen == Int.max { return "" }
        let startIndex = s.index(s.startIndex, offsetBy: minLeft)
        let endIndex = s.index(s.startIndex, offsetBy: minLeft + minLen)
        return String(s[startIndex..<endIndex])
    }
}
