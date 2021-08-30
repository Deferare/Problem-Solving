class Solution {
    func truncateSentence(_ s: String, _ k: Int) -> String {
        let arr = s.split(separator: " ")
        var result = ""
        for i in 0..<k{
            result += arr[i]
            if i != k-1{
                result += " "
            }
        }
        return result
    }
}
