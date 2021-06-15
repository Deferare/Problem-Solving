fun main(args: Array<String>) {
    var n = readLine()!!.toInt()
    var cnt = 0
    for (i in 0 until n) {
        var str = readLine()
        var check = 0
        loop@for (i in 0 until str!!.length-1) {
            if (i != 0) {
                if (str[i] != str[i+1]) {
                    for (j in 0 until i) {
                        if (str[j] == str[i+1]) {
                            check = 1
                            break@loop
                        }
                    }
                }
            }
        }
        if (check == 0) cnt++
    }
    print(cnt)
}
