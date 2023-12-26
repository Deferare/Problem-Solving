import Foundation

func solution(_ s:String) -> Int {
    let sArr = Array(s)
    var result: [Character] = []
    var i = 0
    
    while i < sArr.count {
        if sArr[i] == "z" {
            result.append("0")
            i += 4
        } else if sArr[i] == "o" {
            result.append("1")
            i += 3
        } else if sArr[i] == "t" {
            if sArr[i+1] == "w" {
                result.append("2")
                i += 3
            } else if sArr[i+1] == "h" {
                result.append("3")
                i += 5
            }
        } else if sArr[i] == "f" {
            if sArr[i+1] == "o" {
                result.append("4")
                i += 4
            } else if sArr[i+1] == "i" {
                result.append("5")
                i += 4
            }
        } else if sArr[i] == "s" {
            if sArr[i+1] == "i" {
                result.append("6")
                i += 3
            } else if sArr[i+1] == "e" {
                result.append("7")
                i += 5
            }
        } else if sArr[i] == "e" {
            result.append("8")
            i += 5
        } else if sArr[i] == "n" {
            result.append("9")
            i += 4
        } else {
            result.append(sArr[i])
            i += 1
        }
    }
    
    return Int(String(result))!
}
