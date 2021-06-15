var data = [Int](repeating: 0, count: 100)
func factori(n:Int) -> Int{
    if (n == 0){
        return 1
    }
    if (n == 1){
        return 1
    }
    if (data[n] != 0) {
        return data[n]
    }
    data[n] = factori(n: n-1) * n
    return data[n]
}
print(factori(n: Int(readLine()!)!))
