class Solution {
    func canBeEqual(_ target: [Int], _ arr: [Int]) -> Bool {
        var dict = Dictionary<Int,Int>()
        for i in 0..<target.count{
            if dict[target[i]] == nil{
                dict[target[i]] = 1
            }else{
                dict[target[i]]! += 1
            }
            if dict[arr[i]] == nil{
                dict[arr[i]] = -1
            }else{
                dict[arr[i]]! -= 1
            }
        }
        for crnt in dict.values{
            if crnt != 0{
                return false
            }
        }
        return true
    }
}
