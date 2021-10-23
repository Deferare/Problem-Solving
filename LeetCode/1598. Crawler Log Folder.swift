extension String {
    func get(_ n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func minOperations(_ logs: [String]) -> Int {
        var location = 0
        for log in logs{
            if log.get(1) == "."{
                if location > 0{
                    location -= 1
                }
            }
            else if log.count == 2 && log.get(0) == "."{
                continue
            }
            else{
                location += 1
            }
        }
        return location
    }
}
