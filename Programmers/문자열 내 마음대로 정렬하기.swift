func solution(_ strings:[String], _ n:Int) -> [String] {
    let strings = strings.map { Array($0) }
    
    let result = strings.sorted { a, b in
        if a[n] < b[n] { return true }
        else if a[n] > b[n] { return false }
        return String(a) < String(b)
    }
    
    return result.map{String($0)}
}
