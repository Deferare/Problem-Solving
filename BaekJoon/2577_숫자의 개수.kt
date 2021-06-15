import java.util.*
fun main(args: Array<String>) {
    var sc:Scanner = Scanner(System.`in`)
    var sum = 1
    for (i in 1..3) {
        sum *= sc.nextInt()
    }
    var saveStr = sum.toString()
    var arr = Array(10,{0})
    for (i in 0 until saveStr.length) {
        arr[saveStr.get(i).toString().toInt()]++
    }
    for (i in 0 until arr.size-1) {
        println(arr[i])
    }
    print(arr[9])
}
