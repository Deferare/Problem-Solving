extension String {
    func get(n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func finalValueAfterOperations(_ operations: [String]) -> Int {
        var result_element = 0
        for operation in operations {
            if operation.get(n: 1) == "+"{
                result_element += 1
            }
            else{
                result_element -= 1
            }
        }
        return result_element
    }
}
