class Solution {
    func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
        var flowerbed = flowerbed
        var cnt = 0
        for i in 0..<flowerbed.count{
            if flowerbed[i] == 0{
                if i != 0 && i != flowerbed.count-1{
                    if flowerbed[i-1] == 0 && flowerbed[i+1] == 0{
                        cnt += 1
                        flowerbed[i] = 1
                    }
                }
                else if i == 0 && i != flowerbed.count-1{
                    if flowerbed[i+1] == 0{
                        cnt += 1
                        flowerbed[i] = 1
                    }
                }
                else if i == flowerbed.count-1 && i != 0{
                    if flowerbed[i-1] == 0{
                        cnt += 1
                        flowerbed[i] = 1
                    }
                }
                else if flowerbed.count < 3{
                    flowerbed[i] = 1
                    cnt += 1
                }
                if cnt >= n{
                    return true
                }
            }
        }
        if cnt >= n{
            return true
        }
        return false
    }
}
