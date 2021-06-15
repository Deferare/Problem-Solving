fun main (args: Array<String>) {
    var n = readLine()!!.toInt()
    var str = readLine()
    var sum = 0
    for (i in 0 until n) {
        sum += str!!.get(i)-'0'
    }
    print(sum)
}
