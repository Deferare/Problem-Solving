extension String {
    func get(_ n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func validPalindrome(_ s: String) -> Bool {
        var arr = [Character]()
        for crnt in s{
            arr.append(crnt)
        }
        var turn = 0
        var leftI = 0; var rightI = arr.count-1
        var life = 1
        var subLeft = 0; var subRight = rightI
        while leftI < rightI{
            let left = arr[leftI]; let right = arr[rightI]
            if left != right{
                life -= 1
                if life < 0{
                    if turn == 1{
                        leftI = subLeft; rightI = subRight
                        turn = 2
                        continue
                    }
                    else{
                        return false
                    }
                }
                if arr[leftI+1] == right && left == arr[rightI-1]{
                    if turn == 0{
                        subLeft = leftI; subRight = rightI-1
                        leftI += 1
                        turn = 1
                    }
                    else{
                        return false
                    }
                }
                else{
                    if arr[leftI+1] == right{
                        leftI += 1
                    }
                    else if left == arr[rightI-1]{
                        rightI -= 1
                    }
                    else if turn == 0{
                        leftI = subLeft; rightI = subRight
                        turn = 2
                        continue
                    }
                    else{
                        return false
                    }
                }
            }
            else{
                leftI += 1
                rightI -= 1
            }
        }
        return true
    }
}
