extension String {
    func get(_ n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func longestPalindrome(_ s: String) -> Int {
        var dict = [String:Int]()
        for i in 0..<s.count{
            let ele = String(s.get(i))
            if dict[ele] == nil{
                dict[ele] = 1
            }
            else{
                dict[ele]! += 1
            }
        }
        var oddCheck = 0
        var odd = 0
        var cnt = 0
        for (_,value_d) in dict{
            if value_d == 1{
                oddCheck = 1
            }
            else{
                if value_d%2 != 0{
                    odd += value_d-1
                }
                else{
                    cnt += value_d
                }
            }
        }
        if odd > 0 && oddCheck == 0{
            odd += 1
        }
        return cnt+oddCheck+odd
    }
}
