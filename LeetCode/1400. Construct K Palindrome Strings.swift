class Solution {
    func canConstruct(_ s: String, _ k: Int) -> Bool {
        let s:[Character] = Array(s)
        if s.count < k {return false}
        if s.count == k {return true}
        
        var dict = Dictionary<Character, Int>()
        
        for c in s{
            dict[c, default: 0] += 1
        }
        
        var oddCount = 0
        
        for (_, count) in dict{
            if count%2 != 0 {oddCount += 1}
        }
        
        if oddCount > k {return false}
        
        return true
    }
}
