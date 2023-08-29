class Solution {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        if hand.count%groupSize != 0 {return false}
        
        var counter = Dictionary<Int,Int>()
        for num in hand {counter[num, default: 0] += 1}
        let sortedNum = hand.sorted()
        
        for num in sortedNum {
            if counter[num] == nil {continue}
            
            for i in num..<num+groupSize{
                if counter[i] == nil {return false}
                counter[i]! -= 1
                if counter[i]! == 0 {counter[i] = nil}
            }
        }
        
        return true
    }
}
