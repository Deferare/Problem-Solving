extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func interpret(_ command: String) -> String {
        var result = ""
        var i = 0
        while i < command.count{
            if command.get(n: i) != "("{
                result += String(command.get(n: i))
            }
            else{
                i += 1
                if command.get(n: i) != ")"{
                    while command.get(n: i) != ")" && i < command.count{
                        result += String(command.get(n: i))
                        i += 1
                    }
                }
                else{
                    result += "o"
                }
            }
            i += 1
        }
        return result
    }
}
