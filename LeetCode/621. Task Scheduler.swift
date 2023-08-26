class Solution {
    func leastInterval(_ tasks: [Character], _ n: Int) -> Int {
        var taskCounts = Dictionary<Character, Int>()
        var maxFrequency = 0, maxFrequencyTasks = 0
        
        for task in tasks {
            taskCounts[task, default: 0] += 1
            if taskCounts[task]! > maxFrequency {
                maxFrequency = taskCounts[task]!
                maxFrequencyTasks = 1
            }else if taskCounts[task]! == maxFrequency{
                maxFrequencyTasks += 1
            }
        }
        
        return max(tasks.count, (maxFrequency-1) * (n+1) + maxFrequencyTasks)
    }
}
