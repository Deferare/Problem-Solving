func solution(_ s:String, _ n:Int) -> String {
    var result: Array<Character> = []
    
    for c in s.unicodeScalars {
        var cUni = Int(c.value)
        if cUni == 32 {
            result.append(" ")
        } else {
            if cUni < 97 {
                cUni += n
                if cUni > 90 {
                    cUni %= 90
                    cUni += 64
                }
            } else {
                cUni += n
                if cUni > 122 {
                    cUni %= 122
                    cUni += 96
                }
            }
            
            result.append(Character(UnicodeScalar(cUni)!))
        }
    }
    
    return String(result)
}
