let plates = Array(readLine()!)
var result = 10

for i in 1..<plates.count{
    if plates[i] != plates[i-1]{
        result += 10
    }
    else{
        result += 5
    }
}

print(result)
