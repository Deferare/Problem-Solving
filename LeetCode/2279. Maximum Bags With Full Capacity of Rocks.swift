class Solution {
    func maximumBags(_ capacity: [Int], _ rocks: [Int], _ additionalRocks: Int) -> Int {
        var addedNumber = 0
        var differences = [Int]()
        for i in 0..<capacity.count{
            let differ = capacity[i] - rocks[i]
            if differ != 0{
                differences.append(differ)
            }else{
                addedNumber += 1
            }
        }
        
        differences.sort()
        
        var addableRocks = additionalRocks
        for i in 0..<differences.count{
            if addableRocks >= differences[i]{
                addableRocks -= differences[i]
                addedNumber += 1
            }else{
                break
            }
        }
        
        return addedNumber
    }
}
