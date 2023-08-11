class Solution {
    func largestValsFromLabels(_ values: [Int], _ labels: [Int], _ numWanted: Int, _ useLimit: Int) -> Int {
        let labeledValues = zip(values, labels).sorted(by: >)
        var labelCount: [Int: Int] = [:]
        var sum = 0
        var numWanted = numWanted

        for pair in labeledValues {
            if numWanted == 0 { break }
            if labelCount[pair.1] == nil || labelCount[pair.1]! < useLimit{
                sum += pair.0
                labelCount[pair.1, default: 0] += 1
                numWanted -= 1
            }
        }

        return sum
    }
}
