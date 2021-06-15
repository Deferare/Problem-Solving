import java.util.*
fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    val arr = IntArray(n)
    for (i in arr.indices) {
        arr[i] = sc.nextInt()
    }
    var max = -1001
    var tmp = -1001
    val turn = 0
    for (i in arr.indices) {
        if (tmp > arr[i] || tmp == -1001 || tmp < tmp + arr[i]) {
            if (tmp == -1001) tmp = 0
            tmp += arr[i]
        }
        if (tmp <= arr[i]) {
            tmp = 0
            tmp += arr[i]
        }
        if (tmp > max) max = tmp
    }
    println(max)
}
