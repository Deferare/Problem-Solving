class Solution {
    func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
        let g = g.sorted(); let s = s.sorted()
        var result = 0
        var candyIndex = 0
        for i in 0..<min(s.count, g.count){
            for j in candyIndex..<s.count{
                if g[i] <= s[j]{
                    result += 1
                    candyIndex = j+1
                    break
                }
            }
        }
        return result
    }
}
