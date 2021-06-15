import java.util.*
fun main() {
        val sc = Scanner(System.`in`)
        val str = sc.nextLine()
        val n = sc.nextInt()
        sc.nextLine()
        var result = 0
        for (i in 0 until n) {
            val ring = sc.nextLine()
            for (j in 0 until ring.length) {
                if (str[0] == ring[j]) {
                    var check = 0
                    var index = 0
                    var k = j
                    while (k < j + str.length) {
                        if (k == ring.length) {
                            k = 0
                        }
                        if (ring[k] != str[index]) {
                            check = 1
                            break
                        }
                        index++
                        if (index >= str.length) break
                        k++
                    }
                    if (check == 0) {
                        result++
                        break
                    }
                }
            }
        }
        print(result)
    }
