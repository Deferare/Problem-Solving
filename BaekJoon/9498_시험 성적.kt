import java.util.*
fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    if (n >= 90)
        println("A")
    else if (n > 79 && n < 90)
        println("B")
    else if (n > 69 && n < 80)
        println("C")
    else if (n > 59 && n < 70)
        println("D")
    else println("F")
}
