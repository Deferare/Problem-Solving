fun main() {
    val arr = mutableListOf<String>()
    for (i in 0..7){
        arr.add(readLine().toString())
    }
    var check = 0
    for (i in 1..8){
        var bias = 1
        if (i%2 != 0){
            bias = 0
        }
        for (j in 1+bias..8 step(2)){
            if (arr[i-1][j-1].equals('F')){
                check += 1
            }
        }
    }
    print(check)
}
