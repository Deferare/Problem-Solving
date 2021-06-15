import Foundation
extension String {
    func get(n:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
var input = readLine()!.split(separator: " ")
var a:String = String(input[0]); var b:String = String(input[1])
var minMain = 0
for i in 0 ... b.count-a.count {
    var saveStr = ""; var minCheck = 0
    for j in i ... i+a.count-1 {
        saveStr += String(b.get(n: j))
    }
    for j in 0 ... a.count-1{
        if (a.get(n: j) == saveStr.get(n: j)) {
            minCheck += 1
        }
    }
    if (minCheck > minMain) {
        minMain = minCheck
    }
}
print(a.count-minMain)
