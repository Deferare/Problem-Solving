class Solution {
    func minProcessingTime(_ processorTime: [Int], _ tasks: [Int]) -> Int {
        let sortedProcessorTime = processorTime.sorted()
        let sortedTasks = tasks.sorted(by: >)
        var result = 0
        
        for (i, processor) in sortedProcessorTime.enumerated() {
            result = max(result,
                         processor + sortedTasks[i*4],
                         processor + sortedTasks[i*4+1],
                         processor + sortedTasks[i*4+2],
                         processor + sortedTasks[i*4+3])
        }
        
        return result
    }
}
