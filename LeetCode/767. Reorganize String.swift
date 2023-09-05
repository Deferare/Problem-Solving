class Solution {
    func reorganizeString(_ s: String) -> String {
        var counter:[String:Int] = [:]
        for c in s { counter[c.description, default: 0] += 1 }
        
        var arr = counter.map { (char, count) in return (char: char, count: count) }
        
        var result:[String] = []
        
        while arr.count > 0 {
            arr.sort(by: {$0.count < $1.count})
            
            var pop = arr.popLast()
            
            if pop?.count ?? 0 == 0 { return "" }
            
            if pop?.char != result.last {
                result.append(pop!.char)
                pop!.count -= 1
            } else {
                var pop2 = arr.popLast()
                if pop2?.count ?? 0 == 0 { return "" }
                result.append(pop2!.char)
                pop2!.count -= 1
                
                if pop2!.count > 0 { arr.append(pop2!) }
            }
            
            if pop!.count > 0 { arr.append(pop!) }
        }
        
        return result.joined()
    }
}
