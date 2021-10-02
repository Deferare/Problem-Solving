class Solution {
    func commonChars(_ words: [String]) -> [String] {
        var arr = Array<Dictionary<Character,Int>>()
        for i in 1..<words.count{
            var subDict = Dictionary<Character,Int>()
            for crnt in words[i]{
                if subDict[crnt] != nil{
                    subDict[crnt]! += 1
                }
                else{
                    subDict[crnt] = 1
                }
            }
            arr.append(subDict)
        }
        var result = Array<String>()
        for ChrMain in words[0]{
            for i in 0..<arr.count{
                if arr[i][ChrMain] != nil && arr[i][ChrMain]! > 0{
                    if i == arr.count-1{
                        result.append(String(ChrMain))
                    }
                    arr[i][ChrMain]! -= 1
                    continue
                }
                else{
                    break
                }
            }

        }
        return result
    }
}
