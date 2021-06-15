var memo = [Int](repeating: -1, count: 50)
var testCase = Int(readLine()!)!
for i in 0...testCase-1 {
    var n = Int(readLine()!)!
    func pabo(n:Int) -> Int {
        if (n <= 0) {
            return 0
        }
        else if (n == 1) {
            return 1
        }
        if (memo[n] > -1) {
            return memo[n]
        }
        memo[n] = pabo(n: n-1) + pabo(n: n-2)
        var put = pabo(n: n-1) + pabo(n: n-2)
        return put
    }
    if (n == 0) {
        print("\(1) \(0)")
    }
    else if (n == 1) {
        print("\(0) \(1)")
    }
    else {
        print("\(pabo(n: n-1)) \(pabo(n: n))")
    }
}
