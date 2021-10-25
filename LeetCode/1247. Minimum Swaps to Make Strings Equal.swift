extension String {
    func get(_ n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func minimumSwap(_ s1: String, _ s2: String) -> Int {
        var arr = [Int]()
        for i in 0..<s1.count{
            if (s1.get(i) != s2.get(i)){
                if s1.get(i) == "x"{
                    arr.append(1)
                }
                else{
                    arr.append(0)
                }
            }
        }
        var result_cnt = 0
        while arr.count > 0{
            var check = 0
            for i in 0..<arr.count-1{
                if arr[i] != -1{
                    for j in i+1..<arr.count{
                        if arr[j] != -1{
                            if arr[i] == arr[j]{
                                arr[i] = -1
                                arr[j] = -1
                                result_cnt += 1
                                check = 1
                                break
                            }
                            else{
                                break
                            }
                        }
                    }
                    if check == 1{
                        break
                    }
                }
            }
            if check != 1{
                break
            }
        }
        var cnt = 0
        for arr in arr {
            if arr != -1{
                cnt += 1
            }
        }
        if cnt%2 != 0{
            return -1
        }
        if cnt > 2{
            let sub_cacu = Int(cnt/2)
            result_cnt += sub_cacu
            if sub_cacu%2 != 0{
                result_cnt += 1
            }
        }
        else{
            result_cnt += (2*(Int(cnt/2)))
        }

        return result_cnt
    }
}
