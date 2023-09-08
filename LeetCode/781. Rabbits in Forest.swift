class Solution {
    func numRabbits(_ answers: [Int]) -> Int {
        var count: Dictionary<Int, Int> = [:]
        for answer in answers {
            count[answer, default: 0] += 1
        }
        
        var result = 0
        for (key,value) in count {
            result += ((value/(key+1))+min(1, value%(key+1))) * (key+1)
        }
        
        return result
    }
}
