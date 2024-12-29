class Solution {
    func maxPalindromesAfterOperations(_ words: [String]) -> Int {
        var totalCounts = [Int](repeating: 0, count: 26)
        var totalPairs = 0
        var totalSingles = 0
        
        for word in words {
            for ch in word {
                let idx = Int(ch.asciiValue! - Character("a").asciiValue!)
                totalCounts[idx] += 1
            }
        }
        
        for count in totalCounts {
            totalPairs += count / 2
            totalSingles += count % 2
        }
        
        var wordsNeeded = [(pNeeded: Int, sNeeded: Int)]()
        
        for word in words {
            let L = word.count
            let pNeeded = L / 2
            let sNeeded = L % 2
            wordsNeeded.append((pNeeded, sNeeded))
        }
        
        wordsNeeded.sort { $0.pNeeded < $1.pNeeded }
        
        var usedPairs = 0
        var requiredSingles = 0
        var maxPalindromes = 0
        
        for word in wordsNeeded {
            let pNeeded = word.pNeeded
            let sNeeded = word.sNeeded
            
            if usedPairs + pNeeded <= totalPairs {
                usedPairs += pNeeded
                requiredSingles += sNeeded
                maxPalindromes += 1
            } else {
                break
            }
        }
        
        return maxPalindromes
    }
}
