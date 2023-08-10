class Solution {
    func matchPlayersAndTrainers(_ players: [Int], _ trainers: [Int]) -> Int {
        let players = players.sorted(by: <)
        let trainers = trainers.sorted(by: <)
        let (pLen, tLen) = (players.count, trainers.count)
        
        var matches = 0
        var (i, j) = (0,0)
        
        while i < pLen && j < tLen {
            if players[i] <= trainers[j] {
                i += 1
                matches += 1
            }
            j += 1
        }
        
        return matches
    }
}
