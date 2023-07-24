class Solution {
    func minSetSize(_ arr: [Int]) -> Int {
        var dict = Dictionary<Int, Int>()
        var newArr = [Int]()
        var removeCount = 0
        var removedLenght = arr.count
        let halfLenght = arr.count/2
        
        for num in arr{
            dict[num, default: 0] += 1
        }
        
        for (_, value) in dict{
            newArr.append(value)
        }
        newArr.sort(by: >)
        
        for num in newArr{
            removedLenght -= num
            removeCount += 1
            if removedLenght <= halfLenght {break}
        }
        
        return removeCount
    }
}
