class Solution {
    func longestString(_ x: Int, _ y: Int, _ z: Int) -> Int {
        var result = (min(x, y) + min(x, y) + z) * 2
        if x != y { result += 2 }
        
        return result
    }
}
