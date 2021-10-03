class Solution {
    func countCharacters(_ words: [String], _ chars: String) -> Int {
        var dict_init = Dictionary<Character,Int>()
        for chr in chars{
            if dict_init[chr] == nil{
                dict_init[chr] = 1
            }
            else{
                dict_init[chr]! += 1
            }
        }
        var result = 0
        for word in words{
            var dict = dict_init
            var cnt = word.count
            for chr in word{
                if dict[chr] == nil{
                    cnt = -1
                    break
                }
                else{
                    dict[chr]! -= 1
                    if dict[chr] == 0{
                        dict[chr] = nil
                    }
                }
            }
            if cnt != -1{
                result += cnt
            }
        }
        return result
    }
}
