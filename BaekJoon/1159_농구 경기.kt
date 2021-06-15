fun main() {
    var n = readLine()!!.toInt()
    var strArr = Array(n,{""})
    for (i in 0 .. n-1) {
        strArr[i] = readLine().toString()
    }
    var checker = IntArray(26)
    for (i in 0 .. strArr.size-1) {
        checker[strArr[i][0].toInt()-97]++
    }
    var alpabet = CharArray(26)
    for (i in 0 .. 25) {
        alpabet[i] = (97+i).toChar()
    }
    var result = ""
    for (i in 0 .. checker.size-1) {
        if (checker[i] > 4) {
            result += alpabet[i]
        }
    }
    if (result.length != 0) {
        print(result)
    }
    else {
        print("PREDAJA")
    }
}
