class Solution {
    func checkIfCanBreak(_ s1: String, _ s2: String) -> Bool {
        let arr1 = Array(s1).sorted()
        let arr2 = Array(s2).sorted()
        let n = arr1.count
        
        var check1 = true
        var check2 = true
        
        for i in 0...n{
            if !(check1 || check2){break}
            if i == n {return true}
            
            if check1 && arr1[i] > arr2[i]{
                check1 = false
            }
            if check2 && arr1[i] < arr2[i]{
                check2 = false
            }
        }
        
        return false
    }
}
