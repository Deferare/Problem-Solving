class Solution {
    func findOriginalArray(_ changed: [Int]) -> [Int] {
        if changed.count % 2 != 0 { return [] }
        
        var counter = Dictionary<Int, Int>()
        
        for num in changed {
            counter[num, default: 0] += 1
        }
        
        let sortedKeys = counter.keys.sorted()

        var original = [Int]()
        
        for key in sortedKeys {
            while let count = counter[key], count > 0 {
                let subKey = key * 2
                if let subCount = counter[subKey], subCount > 0 {
                    original.append(key)
                    
                    counter[key]! -= 1
                    counter[subKey]! -= 1
                } else {
                    return []
                }
            }
        }
        
        return original
    }
}
