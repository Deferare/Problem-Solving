import java.util.*
fun main(args: Array<String>) {
    var sc:Scanner = Scanner(System.`in`)
    var testCase = sc.nextInt()
    var resultArr = Array(testCase,{0})
    for (i in 0 until testCase) {
        var str = sc.next()
        var name = str.split(",")
        resultArr[i] = name[0].toInt() + name[1].toInt()
    }
    for (i in 0 until resultArr.size-1) {
        println(resultArr[i])
    }
    print(resultArr[resultArr.size-1])
}
