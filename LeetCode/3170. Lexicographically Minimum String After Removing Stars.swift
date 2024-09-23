import Collections

class Solution {
    func clearStars(_ s: String) -> String {
        var charHeap: Heap<Character> = Heap()
        var charIndices: Dictionary<Character, [Int]> = [:]
        var resultArray: [Character] = Array(s)
        
        for (i, char) in s.enumerated() {
            if char == "*" {
                let minChar = charHeap.removeMin()
                let minIndex = charIndices[minChar]!.removeLast()
                
                resultArray[minIndex] = " "
                resultArray[i] = " "
            } else {
                charHeap.insert(char)
                
                if charIndices[char] == nil {
                    charIndices[char] = [i]
                } else {
                    charIndices[char]!.append(i)
                }
            }
        }
        
        return String(resultArray.filter {
            $0 != " " && $0 != "*"
        })
    }
}
