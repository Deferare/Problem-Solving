import java.util.*
fun main(args: Array<String>) {
    var sc:Scanner = Scanner(System.`in`)
    var str: String = sc.nextLine()
    var check = 0
    for (i in 0 until str.length) {
        if (str.get(i) == ' ') {
            check++
        }
    }
    if (str.get(0) == ' ') check--
    if (str.get(str.length-1) == ' ') check--
    print(check+1)
}
