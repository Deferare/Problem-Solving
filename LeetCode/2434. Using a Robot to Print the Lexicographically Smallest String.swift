class Solution {
    func robotWithString(_ s: String) -> String {
        let s = Array(s)
        var t = [Character]()
        var result = [Character]()
        var freq = Array(repeating: 0, count: 26)
        var minChar: Character = "a"

        for char in s {
            freq[Int(char.asciiValue! - 97)] += 1
        }
        
        func updateMinChar() {
            while Int(minChar.asciiValue! - 97) < 26 && freq[Int(minChar.asciiValue! - 97)] == 0 {
                minChar = Character(UnicodeScalar(minChar.asciiValue! + 1))
            }
        }
        
        for char in s {
            while !t.isEmpty && t.last! <= minChar {
                result.append(t.removeLast())
            }
            
            t.append(char)
            
            freq[Int(char.asciiValue! - 97)] -= 1
            updateMinChar()
        }
        
        result.append(contentsOf: t.reversed())
        
        return String(result)
    }
}
