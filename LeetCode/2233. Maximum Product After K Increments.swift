import Collections

class Solution {
    func maximumProduct(_ nums: [Int], _ k: Int) -> Int {
        var heap = Heap<Int>(nums)
        var k = k
        
        while k > 0, let pop = heap.popMin() {
            heap.insert(pop + 1)
            k -= 1
        }
        
        var maxProduct = heap.popMax() ?? 1
        
        for num in heap.unordered {
            maxProduct = (num * maxProduct) % 1_000_000_007
        }
        
        return maxProduct
    }
}
