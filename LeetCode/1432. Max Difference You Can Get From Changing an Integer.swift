class Solution {
    func maxDiff(_ num: Int) -> Int {
        let number = Array(String(num))
        var targetNum: Character = "-"
        var a = [Character]()
        var b = [Character]()
        
        for n in number {
            if targetNum == "-" && n != "9" {
                targetNum = n
            }
            
            if n == targetNum {
                a.append("9")
            } else {
                a.append(n)
            }
        }
        
        targetNum = "-"
        var toNum: Character = "-"
        
        for (i, n) in number.enumerated() {
            if targetNum == "-" && n != "1" && n != "0" {
                toNum = i == 0 ? "1" : "0"
                targetNum = n
            }
            
            if n == targetNum && targetNum != "-" {
                b.append(toNum)
            } else {
                b.append(n)
            }
        }
        
        let maxNumber = Int(String(a)) ?? 0
        let minNumber = Int(String(b)) ?? 0
        
        return maxNumber - minNumber
    }
}
