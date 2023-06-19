class Solution {
    func findSubstring(_ s: String, _ words: [String]) -> [Int] {
        let sArray = Array(s)
        let sLen = sArray.count
        let wordLen = words[0].count
        var wordsCounterOriginal = Dictionary<String, Int>()
        
        for word in words {
            if wordsCounterOriginal[word] == nil{
                wordsCounterOriginal[word] = 1
            }else{ wordsCounterOriginal[word]! += 1 }
        }
        
        var answer = [Int]()
        var wordsCounter = wordsCounterOriginal
        var mainInx = 0
        var inx = 0
        
        while inx <= sLen - wordLen{
            let c = String(sArray[inx..<inx + wordLen])
            if wordsCounter[c] != nil{
                wordsCounter[c]! -= 1
                if wordsCounter[c]! == 0{
                    wordsCounter.removeValue(forKey: c)
                }
                if wordsCounter.isEmpty{
                    answer.append(mainInx)
                    wordsCounter = wordsCounterOriginal
                    mainInx += 1
                    inx = mainInx
                }else{
                    inx += wordLen
                }
            }else{
                mainInx += 1
                inx = mainInx
                wordsCounter = wordsCounterOriginal
            }
        }

        return answer
    }
}
