class Solution {
    func xor_convertor(_ first:Int,_ second:Int) -> String{
        let first_bin = Array(String(first, radix: 2))
        let second_bin = Array(String(second, radix: 2))
        var result = ""
        for i in 1...max(first_bin.count, second_bin.count){
            if first_bin.count-i < 0 && second_bin.count-i >= 0{
                for j in (0...second_bin.count-i).reversed(){
                    if second_bin[j] == "1"{
                        result = "1"+result
                    }
                    else{
                        result = "0"+result
                    }
                }
                break
            }
            else if second_bin.count-i < 0 && first_bin.count-i >= 0{
                for j in (0...first_bin.count-i).reversed(){
                    if first_bin[j] == "1"{
                        result = "1"+result
                    }
                    else{
                        result = "0"+result
                    }
                }
                break
            }
            else{
                if first_bin[first_bin.count-i] != second_bin[second_bin.count-i]{
                    result = "1"+result
                }
                else{
                    result = "0"+result
                }
            }
        }
        return result
    }


    func decode(_ encoded: [Int], _ first: Int) -> [Int] {
        var result = [first]
        for i in 0..<encoded.count{
            result.append(Int(xor_convertor(result[result.count-1], encoded[i]), radix: 2)!)
        }
        return result
    }
}
