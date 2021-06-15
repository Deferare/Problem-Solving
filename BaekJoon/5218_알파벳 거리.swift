import Foundation
extension String {
    func get(n:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
var n = Int(readLine()!)
for _ in 0...n!-1 {
    var put = readLine()!.split(separator: " ")
    var str1 = String(put[0]); var str2 = String(put[1])
    var result = ""
    for i in 0...str1.count-1 {
        if (str1.get(n: i).asciiValue! <= str2.get(n: i).asciiValue!) {
            result += String(str2.get(n: i).asciiValue! - str1.get(n: i).asciiValue!)
        }
        else if (str1.get(n: i).asciiValue! > str2.get(n: i).asciiValue!) {
            var save:Int = Int(str1.get(n: i).asciiValue! - str2.get(n: i).asciiValue!)
            result += String(26-save)
        }
        if (i != str1.count-1) {
            result += " "
        }
    }
    print("Distances: \(result)")
}
