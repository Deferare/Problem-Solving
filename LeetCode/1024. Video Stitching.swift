class Solution {
    func videoStitching(_ clips: [[Int]], _ time: Int) -> Int {
        let sortedClips = clips.sorted(by: { $0[0] < $1[0] })
        var end = 0
        var count = 0
        var i = 0
        
        while end < time {
            if i >= sortedClips.count || sortedClips[i][0] > end { return -1 }
            var maxEnd = end
            while i < sortedClips.count && sortedClips[i][0] <= end {
                maxEnd = max(maxEnd, sortedClips[i][1])
                i += 1
            }
            end = maxEnd
            count += 1
        }
        
        return count
    }
}
