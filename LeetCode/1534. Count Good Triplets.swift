class Solution {
    func countGoodTriplets(_ arr: [Int], _ a: Int, _ b: Int, _ c: Int) -> Int {
        let arrLen = arr.count
        var result = 0
        for i in 0...arrLen-3{
            for j in i+1...arrLen-2{
                for k in j+1...arrLen-1{
                    if abs(arr[i]-arr[j]) <= a && abs(arr[j]-arr[k]) <= b && abs(arr[i]-arr[k]) <= c{
                        result += 1
                    }
                }
            }
        }
        return result
    }
}
