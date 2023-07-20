class Solution {
    func getMinSwaps(_ num: String, _ k: Int) -> Int {
        let original:[Character] = Array(num)
        var kthSmallest:[Character] = Array(num)
        
        for _ in 0..<k{
            self.nextSmallest(&kthSmallest)
        }

        var swapCount = 0

        for i in 0..<original.count{
            var pre = original[i]
            var inx = i

            while inx < kthSmallest.count && original[i] != kthSmallest[inx]{
                let tmp = kthSmallest[inx]
                kthSmallest[inx] = pre
                pre = tmp
                inx += 1
                swapCount += 1
            }
            
            kthSmallest[inx] = pre
        }
        
        return swapCount
    }
    
    private func nextSmallest(_ arr: inout [Character]){
        var left = arr.count - 1

        while left > 0 && arr[left - 1] >= arr[left]{
            left -= 1
        }

        if left != 0{
            var right = arr.count - 1

            while right > left && arr[left - 1] >= arr[right]{
                right -= 1
            }

            arr.swapAt(left - 1, right)
            arr[left...].reverse()
        }
    }
}
