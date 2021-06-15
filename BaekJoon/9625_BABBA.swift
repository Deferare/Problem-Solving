var n = Int(readLine()!)!
var result = 0
var str:String = "A"
var arr = [Int](repeating: 0, count: 50)
arr[0] = 1; arr[1] = 1

if n == 1 {
    print("\(0) \(1)")
}
else {
    for i in 2...n {
        arr[i] = arr[i-1] + arr[i-2]
    }
    print("\(arr[n]-arr[n-1]) \(arr[n-1])")
}
