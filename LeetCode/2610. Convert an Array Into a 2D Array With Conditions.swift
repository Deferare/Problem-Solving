class Solution {
    func findMatrix(_ nums: [Int]) -> [[Int]] {
        var numsCounter = Dictionary<Int, Int>()
        for num in nums {
            numsCounter[num, default: 0] += 1
        }
        
        var answer = [[Int]]()
        while !numsCounter.isEmpty{
            var arr = [Int]()
            for (n, _) in numsCounter{
                arr.append(n)
                numsCounter[n]! -= 1
                if numsCounter[n]! < 1 {numsCounter[n] = nil}
            }
            answer.append(arr)
        }
        
        return answer
    }
}
