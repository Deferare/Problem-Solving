class Solution {
    func lemonadeChange(_ bills: [Int]) -> Bool {
        var money_recived = [0,0,0]
        for i in 0..<bills.count{
            if bills[i] == 5{
                money_recived[2] += 1
            }
            else{
                if bills[i] == 20{
                    if money_recived[1] >= 1 && money_recived[2] >= 1{
                        money_recived[1] -= 1
                        money_recived[2] -= 1
                    }
                    else if money_recived[2] >= 3{
                        money_recived[2] -= 3
                    }
                    else{
                        return false
                    }
                }
                else if money_recived[2] >= 1{
                    money_recived[1] += 1
                    money_recived[2] -= 1
                }
                else{
                    return false
                }
            }
        }
        return true
    }
}
