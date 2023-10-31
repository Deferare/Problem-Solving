class Solution {
    func maxProfitAssignment(_ difficulty: [Int], _ profit: [Int], _ worker: [Int]) -> Int {
        var jobs: [(diffic: Int, prof: Int)] = []
        for i in 0..<difficulty.count { jobs.append((difficulty[i], profit[i])) }
        jobs.sort { $0.1 > $1.1 }
        
        let worker = worker.sorted(by: >)
        var answer = 0
        var i = 0
        
        for ability in worker {
            while i < jobs.count {
                if ability >= jobs[i].diffic {
                    answer += jobs[i].prof
                    break
                }
                i += 1
            }
        }
        
        return answer
    }
}
