class Solution {
    func judgeCircle(_ moves: String) -> Bool {
        let movesLen = moves.count
        if movesLen%2 != 0{
            return false
        }
        var moveRecord = [0,0,0,0]
        for move in moves{
            if move == "R"{
                moveRecord[0] += 1
            }else if move == "L"{
                moveRecord[1] += 1
            }else if move == "U"{
                moveRecord[2] += 1
            }else if move == "D"{
                moveRecord[3] += 1
            }
        }
        if moveRecord[0] != moveRecord[1] || moveRecord[2] != moveRecord[3]{
            return false
        }
        return true
    }
}
