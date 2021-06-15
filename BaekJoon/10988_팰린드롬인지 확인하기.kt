import java.util.*
fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextLine()
    var index = n.length-1
    var check = 0
    for (i in 0..n.length/2){
        if (n[i] != n[index]) {
            check = 1
        }
        index--;
    }
    if (check == 0) {
        println(1)
    }
    else println(0)
}
