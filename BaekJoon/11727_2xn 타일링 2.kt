var data = IntArray(1001)
fun main() {
    val n = readLine()!!.toInt()
    println(fibo(n))
}
fun fibo (n: Int): Int {
    if (1 == n) return 1
    if (2 == n) return 3
    if (data[n] != 0) data[n]
    else data[n] = (fibo(n-1) + 2 * fibo(n-2))%10007
    return data[n]
}
