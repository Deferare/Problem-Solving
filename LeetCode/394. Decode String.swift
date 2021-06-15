class Solution {
func decodeString(_ s: String) -> String {
    let arr = s
    var result = ""
    func dp(arr:String, i:Int) -> String{
        var i = i
        if i >= arr.count {
            return ""
        }
        var value = ""
        if arr.get(index: i).asciiValue! >= 97 && arr.get(index: i).asciiValue! <= 122 {
            value.append(arr.get(index: i))
            value.append(dp(arr: arr, i: i+1))
        }
        else if arr.get(index: i) == "[" {
            value.append(dp(arr: arr, i: i+1))
        }
        else if arr.get(index: i) == "]" {
            value.append(String(i))
        }
        else {
            var index = ""
            var k = i
            while true {
                let number = String(arr.get(index: k))
                if number == "[" {
                    break
                }
                let number2 = Int(String(arr.get(index: k)))
                if number2! >= 0 && number2! <= 9 {
                    index += String(arr.get(index: k))

                    k += 1
                }
                else {
                    break
                }
                
            }
            i = k-1
            var str = dp(arr: arr, i: i+1)
            var n = ""
            for i in (0...str.count-1).reversed() {
                if !(str.get(index: i).asciiValue! >= 97 && str.get(index: i).asciiValue! <= 122) {
                    n += String(str.get(index: i))
                    str.removeLast()
                }
                else {
                    break
                }
            }
            for _ in 0...Int(index)!-1 {
                value.append(str)
            }
            let n2 = n.reversed()
            value.append(dp(arr: arr, i: Int(String(n2))!+1))
        }
        return value
    }
    result = dp(arr: arr, i: 0)
    return result
}
}
extension String {
    func get(index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
