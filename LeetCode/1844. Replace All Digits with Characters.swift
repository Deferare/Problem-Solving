extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func replaceDigits(_ s: String) -> String {
        var resultStr = ""
        let strLen = s.count
        for i in stride(from: 1, to: strLen, by: 2){
            resultStr.append(s.get(n: i-1))
            let index = Int(s.get(n: i-1).asciiValue!) + Int(String(s.get(n: i)))!
            resultStr.append(Character(UnicodeScalar(index)!))
        }
        if strLen%2 != 0{
            resultStr += String(s.get(n: strLen-1))
        }
        return resultStr
    }
}
