var word = Array(readLine()!)
let bomb = Array(readLine()!)

while true{
    var break_check = 0
    var next_word = [Character]()
    for i in 0..<word.count{
        next_word.append(word[i])
        if next_word.count >= bomb.count && word[i] == bomb[bomb.count-1]{
            var check = 0
            for j in 0..<bomb.count{
                if next_word[next_word.count-1-j] != bomb[bomb.count-1-j]{
                    check = 1
                    break
                }
            }
            if check == 0{
                for _ in 0..<bomb.count{
                    next_word.popLast()
                    break_check = 1
                }
            }
        }
    }
    if break_check == 0{
        break
    }
    else{
        word = next_word
    }
}

if word.count == 0{
    print("FRULA")
}
else{
    print(String(word))
}
