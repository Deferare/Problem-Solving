import Foundation

func solution(_ t:String, _ p:String) -> Int {
    let t = Array(t)
    let p = Array(p)
    var result = 0
    
    for i in 0...t.count-p.count {
        for j in 0..<p.count {
            if t[i+j] > p[j] {
                break
            } else if t[i+j] < p[j] {
                result += 1
                break
            } else if j == p.count-1 {
                result += 1
                break
            }
        }
    }
    
    return result
}
