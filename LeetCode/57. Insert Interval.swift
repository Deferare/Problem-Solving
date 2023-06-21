  class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        if intervals.count == 0{return [newInterval]}
        
        var answer = [[Int]]()
        
        for i in 0..<intervals.count{
            if intervals[i][1] < newInterval[0]{
                answer.append(intervals[i])
            }else {
                let new = [min(intervals[i][0], newInterval[0]), intervals[i][1]]
                answer.append(new)
                break
            }
        }
        
        for i in answer.count-1..<intervals.count{
            if intervals[i][1] >= newInterval[1]{
                if intervals[i][0] <= newInterval[1]{
                    answer[answer.count-1][1] = intervals[i][1]
                    answer += intervals[(i+1)...]
                    return answer
                }else{
                    answer[answer.count-1][1] = newInterval[1]
                    answer += intervals[(i)...]
                    return answer
                }
            }
        }
        
        if answer[answer.count-1][1] < newInterval[0]{
            answer.append(newInterval)
        }else{
            answer[answer.count-1][1] = newInterval[1]
        }
        
        return answer
    }
}
