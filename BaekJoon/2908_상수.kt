import java.util.*
fun main (args: Array<String>) {
    var sc = Scanner(System.`in`)
    var a = sc.next()
    var b = sc.next()
    var save1 = ""
    for (i in a!!.length-1 downTo 0) {
        save1 += a.get(i)
    }
    var save2 = ""
    for (i in b!!.length-1 downTo 0) {
        save2 += b.get(i)
    }
    if (save1.toInt() > save2.toInt()) {
        print(save1)
    }
    else print(save2)
}
