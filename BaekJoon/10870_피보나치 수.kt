import java.util.*
var saveData = Array(21, {0})
fun main(args: Array<String>) {
    var sc:Scanner = Scanner(System.`in`)

    var n = sc.nextInt()
    print(cacu(n))
}
fun cacu (n : Int) : Int {
    if (n == 0) return 0
    if (n == 1) return 1
    if (saveData[n] > 0) return saveData[n]
    saveData[n] = cacu(n-1)+cacu(n-2)
    return saveData[n]
}
