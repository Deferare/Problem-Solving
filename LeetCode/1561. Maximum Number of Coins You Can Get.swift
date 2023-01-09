class Solution {
    func maxCoins(_ piles: [Int]) -> Int {
        let pilesSorted = piles.sorted(by: >)
        var answer = 0
        for i in 0..<pilesSorted.count/3{
            let ind = i*2
            answer += pilesSorted[ind+1]
        }
        return answer
    }
}
