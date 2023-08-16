class Solution {
    func maximumEvenSplit(_ finalSum: Int) -> [Int] {
        if finalSum%2 != 0 {return []}
        
        var answer:[Int] = [2]
        var sum = 2
        var crnt = 2
        
        while sum != finalSum {
            crnt += 2
            answer.append(crnt)
            sum += crnt
            
            if sum > finalSum {
                sum -= answer.popLast()!
                crnt = answer.popLast()!
                sum -= crnt
            }
        }
        
        return answer
    }
}
