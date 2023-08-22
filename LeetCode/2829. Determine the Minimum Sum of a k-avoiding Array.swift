class Solution {
    func minimumSum(_ n: Int, _ k: Int) -> Int {
        var sum = 0
        var count = 0
        var skip = Set<Int>()
        var i = 1
        
        while count < n {
            if !skip.contains(i){
                sum += i
                count += 1
                skip.insert(k-i)
            }
            
            i += 1
        }
        
        return sum
    }
}
