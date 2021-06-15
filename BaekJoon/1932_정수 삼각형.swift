extension String {
    func get(n:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
var n = Int(readLine()!)!
var arr = [Array](repeating: [Int](repeating: -1, count: n), count: n)

for i in 0...n-1 {
    var subArr = readLine()!.split(separator: " ")
    for k in 0...subArr.count-1 {
        arr[i][k] = Int(subArr[k])!
    }
}
var max = 0
for i in 0...n-1 {
    for j in 0...i {
        if (i == 0 && j == 0) {
            
        }
        else if (i == j) {
            arr[i][j] += arr[i-1][j-1]
        }
        else if (j == 0) {
            arr[i][j] += arr[i-1][j]
        }
        else {
            arr[i][j] += max(a:arr[i-1][j-1], b:arr[i-1][j])
        }
        if (i == n-1) {
            if (arr[i][j] > max) {
                max = arr[i][j]
            }
        }
    }
}
print(max)
func max(a:Int,b:Int) -> Int {
    if (a > b) {
        return a
    }
    else if (a < b) {
        return b
    }
    return a
}
