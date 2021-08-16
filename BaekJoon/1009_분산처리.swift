let n = Int(readLine()!)
for _ in 0..<n!{
    var input = readLine()!.split(separator: " ").map{Int($0)}
    var a = (input[0]!%10)
    var b = (input[1]!%4)+4
    if input[1] == 0{
        print(1)
        continue
    }
    else if a == 0{
        print(10)
        continue
    }
    for _ in 0..<b-1 {
        a = (a*input[0]!)%10
    }
    print(a)
}
