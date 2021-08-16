class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dict:Dictionary = [Int:Int]()
        for num in nums {
            if (dict[num] == nil) {
                dict[num] = 1
            }
            else{
                dict[num]! += 1
            }
        }
        let dict2 = dict.sorted {$0.1 > $1.1}
        var result = [Int]()
        for i in 0...k-1 {
            result.append(dict2[i].key)
        }
        return result
    }
}
