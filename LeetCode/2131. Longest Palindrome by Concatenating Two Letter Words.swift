class Solution {
    func longestPalindrome(_ words: [String]) -> Int {
        var counter: Dictionary<String, Int> = [:]
        var sameNums: [Int] = []
        var count = 0
        
        for word in words { counter[word, default: 0] += 1 }
        
        for word in words {
            let reversed = String(word.reversed())
            
            if counter[reversed] != nil && counter[word] != nil {
                if word != reversed {
                    counter[word]! -= 1
                    counter[reversed]! -= 1
                    
                    if counter[word]! == 0 { counter[word] = nil }
                    if counter[reversed]! == 0 { counter[reversed] = nil }
                    count += 4
                } else {
                    sameNums.append(counter[reversed]!)
                    counter[reversed] = nil
                }
            }
        }
        
        var sameCount = 0
        var oddExists = false
        for num in sameNums {
            if num%2 == 0 { sameCount += num*2 }
            else if !oddExists {
                sameCount += num*2
                oddExists = true
            } else {
                sameCount += (num-1)*2
            }
        }
        
        return count + sameCount
    }
}
