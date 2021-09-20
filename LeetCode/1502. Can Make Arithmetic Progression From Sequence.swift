class Solution {
    func canMakeArithmeticProgression(_ arr: [Int]) -> Bool {
        let arr = arr.sorted()
        let init_diff = arr[0] - arr[1]
        for i in 1..<arr.count-1{
            let diff = arr[i] - arr[i+1]
            if diff != init_diff{
                return false
            }
        }
        return true
    }
}
