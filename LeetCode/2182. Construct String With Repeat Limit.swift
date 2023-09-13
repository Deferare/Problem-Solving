class Solution {
    func repeatLimitedString(_ s: String, _ repeatLimit: Int) -> String {
        var characterCount = Array(repeating: 0, count: 26)
        for character in s {
            characterCount[Int(character.asciiValue! - Character("a").asciiValue!)] += 1
        }
        
        var result = ""
        var lastCharacter: Character = " "
        var lastCharacterCount = 0
        
        for _ in 0..<s.count {
            for i in stride(from: 25, through: 0, by: -1) {
                if characterCount[i] > 0 && (lastCharacter != Character(UnicodeScalar(i + Int(Character("a").asciiValue!))!) || lastCharacterCount < repeatLimit) {
                    lastCharacter = Character(UnicodeScalar(i + Int(Character("a").asciiValue!))!)
                    lastCharacterCount = lastCharacter == result.last ? lastCharacterCount + 1 : 1
                    characterCount[i] -= 1
                    result.append(lastCharacter)
                    break
                }
            }
            
        }
        
        return result
    }
}
