class Solution {
    func getSmallestString(_ n: Int, _ k: Int) -> String {
        var contain = Array<Character>()
        var n = n
        var k = k
        var crnt = 26
        
        while k > 0{
            while crnt > 0{
                if k - crnt + 1 >= n{
                    contain.append(Character(Unicode.Scalar(crnt + 96)!))
                    k -= crnt
                    n -= 1
                    break
                }
                crnt -= 1
            }
        }
        
        contain.reverse()
        
        return String(contain)
    }
}
