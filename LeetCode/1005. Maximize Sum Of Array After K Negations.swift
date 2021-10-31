class Solution {
    func largestSumAfterKNegations(_ nums: [Int], _ k: Int) -> Int {
        var k = k
        var result = 0
        let myNums = nums.sorted()
        for i in 0..<myNums.count{
            if k > 0{
                if myNums[i] < 0{
                    if i == myNums.count-1{
                        if k%2 == 0{
                            result += myNums[i]
                            break
                        }
                    }
                    result += (myNums[i] * -1)
                }
                else if myNums[i] > 0{
                    if k%2 == 0{
                        result += myNums[i]
                    }
                    else{
                        if i == 0{
                            result += -myNums[i]
                        }
                        else if myNums[i] <= myNums[i-1] * -1{
                            result += -myNums[i]
                        }
                        else{
                            result += (myNums[i-1]+myNums[i-1])
                            result += myNums[i]
                        }
                    }
                    for j in i+1..<myNums.count{
                        result += myNums[j]
                    }
                    break
                }
                else{
                    for j in i..<myNums.count{
                        result += myNums[j]
                    }
                    break
                }
                k -= 1
            }
            else{
                result += myNums[i]
            }
        }
        return result
    }
}
